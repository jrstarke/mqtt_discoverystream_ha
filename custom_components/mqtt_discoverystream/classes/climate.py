"""climate methods for MQTT Discovery Statestream."""
import logging

from homeassistant.components import mqtt
from homeassistant.components.climate import (
    ATTR_CURRENT_TEMPERATURE,
    ATTR_HVAC_ACTION,
    ATTR_HVAC_MODES,
    ATTR_FAN_MODE,
    ATTR_FAN_MODES,
    ATTR_MAX_TEMP,
    ATTR_MIN_TEMP,
    ATTR_PRESET_MODE,
    ATTR_PRESET_MODES,
    ATTR_SWING_MODE,
    ATTR_SWING_MODES,
    ATTR_TARGET_TEMP_STEP,
    PRESET_NONE,
    SERVICE_SET_HVAC_MODE,
    SERVICE_SET_FAN_MODE,
    SERVICE_SET_PRESET_MODE,
    SERVICE_SET_SWING_MODE,
    SERVICE_SET_TEMPERATURE,
)
from homeassistant.components.mqtt.climate import (
    ATTR_HVAC_MODE,
    CONF_ACTION_TOPIC,
    CONF_CURRENT_TEMP_TOPIC,
    CONF_FAN_MODE_COMMAND_TOPIC,
    CONF_FAN_MODE_STATE_TOPIC,
    CONF_FAN_MODE_LIST,
    CONF_MODE_COMMAND_TOPIC,
    CONF_MODE_LIST,
    CONF_MODE_STATE_TOPIC,
    CONF_PRESET_MODE_COMMAND_TOPIC,
    CONF_PRESET_MODE_STATE_TOPIC,
    CONF_PRESET_MODES_LIST,
    CONF_SWING_MODE_LIST,
    CONF_SWING_MODE_COMMAND_TOPIC,
    CONF_SWING_MODE_STATE_TOPIC,
    CONF_TEMP_COMMAND_TOPIC,
    CONF_TEMP_MAX,
    CONF_TEMP_MIN,
    CONF_TEMP_STATE_TOPIC,
    CONF_TEMP_STEP,
)
from homeassistant.const import (
    ATTR_ENTITY_ID,
    ATTR_TEMPERATURE,
    STATE_OFF,
    STATE_UNAVAILABLE,
    Platform,
)

from ..const import ATTR_MODE_COMMAND, ATTR_SWING_COMMAND, ATTR_FAN_COMMAND, ATTR_PRESET_COMMAND, ATTR_TEMP_COMMAND
from ..utils import async_publish_base_attributes

_LOGGER = logging.getLogger(__name__)


class Climate:
    """Climate class."""

    def __init__(self, hass):
        """Initialise the climate class."""
        self._hass = hass

    def build_config(self, config, attributes, mybase, mycommand):
        """Build the config for a climate."""
        config[CONF_ACTION_TOPIC] = f"{mybase}{ATTR_HVAC_ACTION}"
        config[CONF_CURRENT_TEMP_TOPIC] = f"{mybase}{ATTR_CURRENT_TEMPERATURE}"
        config[CONF_TEMP_MAX] = attributes[ATTR_MAX_TEMP]
        config[CONF_TEMP_MIN] = attributes[ATTR_MIN_TEMP]
        config[CONF_MODE_COMMAND_TOPIC] = f"{mycommand}{ATTR_MODE_COMMAND}"
        config[CONF_MODE_LIST] = attributes[ATTR_HVAC_MODES]
        config[CONF_MODE_STATE_TOPIC] = f"{mybase}{ATTR_HVAC_MODE}"
        fan_modes = attributes.get(ATTR_FAN_MODES, None)
        config[CONF_FAN_MODE_LIST] = fan_modes
        config[CONF_FAN_MODE_COMMAND_TOPIC] = f"{mycommand}{ATTR_FAN_COMMAND}"
        config[CONF_FAN_MODE_STATE_TOPIC] = f"{mybase}{ATTR_FAN_MODE}"
        preset_modes = attributes.get(ATTR_PRESET_MODES, None)
        if PRESET_NONE in preset_modes:
            preset_modes.remove(PRESET_NONE)
        config[CONF_PRESET_MODES_LIST] = preset_modes
        config[CONF_PRESET_MODE_COMMAND_TOPIC] = f"{mycommand}{ATTR_PRESET_COMMAND}"
        config[CONF_PRESET_MODE_STATE_TOPIC] = f"{mybase}{ATTR_PRESET_MODE}"
        swing_modes = attributes.get(ATTR_SWING_MODES, None)
        config[CONF_SWING_MODE_LIST] = swing_modes
        config[CONF_SWING_MODE_COMMAND_TOPIC] = f"{mycommand}{ATTR_SWING_COMMAND}"
        config[CONF_SWING_MODE_STATE_TOPIC] = f"{mybase}{ATTR_SWING_MODE}"
        config[CONF_TEMP_COMMAND_TOPIC] = f"{mycommand}{ATTR_TEMP_COMMAND}"
        config[CONF_TEMP_STATE_TOPIC] = f"{mybase}{ATTR_TEMPERATURE}"
        if ATTR_TARGET_TEMP_STEP in attributes:
            step = attributes[ATTR_TARGET_TEMP_STEP]
        else:
            step = 0.5
        config[CONF_TEMP_STEP] = step

    async def async_publish_state(self, new_state, mybase):
        """Publish the state for a light."""
        await self._async_publish_attribute(new_state, mybase, ATTR_HVAC_ACTION, True)
        await self._async_publish_attribute(new_state, mybase, ATTR_CURRENT_TEMPERATURE)
        await self._async_publish_attribute(new_state, mybase, ATTR_PRESET_MODE, True)
        await self._async_publish_attribute(new_state, mybase, ATTR_FAN_MODE, True)
        await self._async_publish_attribute(new_state, mybase, ATTR_SWING_MODE, True)
        await self._async_publish_attribute(new_state, mybase, ATTR_TEMPERATURE)

        await async_publish_base_attributes(self._hass, new_state, mybase)

        payload = new_state.state
        if payload == STATE_UNAVAILABLE:
            payload = STATE_OFF
        await mqtt.async_publish(
            self._hass, f"{mybase}{ATTR_HVAC_MODE}", payload, 1, True
        )

    async def _async_publish_attribute(
        self, new_state, mybase, attribute_name, strip=False
    ):
        if attribute_name in new_state.attributes:
            value = new_state.attributes[attribute_name]
            if value and strip:
                value = value.strip('"')
            await mqtt.async_publish(
                self._hass,
                f"{mybase}{attribute_name}",
                value,
                1,
                True,
            )

    async def async_subscribe(self, command_topic):
        """Subscribe to messages for climate."""
        await self._hass.components.mqtt.async_subscribe(
            f"{command_topic}{Platform.CLIMATE}/+/{ATTR_MODE_COMMAND}",
            self._async_handle_message,
        )
        await self._hass.components.mqtt.async_subscribe(
            f"{command_topic}{Platform.CLIMATE}/+/{ATTR_PRESET_COMMAND}",
            self._async_handle_message,
        )
        await self._hass.components.mqtt.async_subscribe(
            f"{command_topic}{Platform.CLIMATE}/+/{ATTR_FAN_COMMAND}",
            self._async_handle_message,
        )
        await self._hass.components.mqtt.async_subscribe(
            f"{command_topic}{Platform.CLIMATE}/+/{ATTR_SWING_COMMAND}",
            self._async_handle_message,
        )
        await self._hass.components.mqtt.async_subscribe(
            f"{command_topic}{Platform.CLIMATE}/+/{ATTR_TEMP_COMMAND}",
            self._async_handle_message,
        )

    async def _async_handle_message(self, msg):
        """Handle a message for a switch."""
        explode_topic = msg.topic.split("/")
        domain = explode_topic[1]
        entity = explode_topic[2]
        element = explode_topic[3]

        _LOGGER.debug(
            "Message received: topic %s; payload: %s", {msg.topic}, {msg.payload}
        )

        service_payload = {
            ATTR_ENTITY_ID: f"{domain}.{entity}",
        }

        if element == ATTR_MODE_COMMAND:
            service_payload[ATTR_HVAC_MODE] = msg.payload
            service_name = SERVICE_SET_HVAC_MODE
        elif element == ATTR_PRESET_COMMAND:
            service_payload[ATTR_PRESET_MODE] = msg.payload
            service_name = SERVICE_SET_PRESET_MODE
        elif element == ATTR_FAN_COMMAND:
            service_payload[ATTR_FAN_MODE] = msg.payload
            service_name = SERVICE_SET_FAN_MODE
        elif element == ATTR_SWING_COMMAND:
            service_payload[ATTR_SWING_MODE] = msg.payload
            service_name = SERVICE_SET_SWING_MODE
        elif element == ATTR_TEMP_COMMAND:
            service_payload[ATTR_TEMPERATURE] = msg.payload
            service_name = SERVICE_SET_TEMPERATURE

        await self._hass.services.async_call(domain, service_name, service_payload)
