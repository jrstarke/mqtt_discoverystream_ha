# Changelog

## 0.10.5 (2023/01/04)
### Enhancements
- [Added the ability to break out commands into a separate topic structure](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/2f10f38c933d11338e93f39624687d86e5a4af91) - @RogerSelwyn
- [Add temperature step, default 0.5](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/672773a476dc538d9658d0db6c156061501d2991) - @RogerSelwyn
### Maintenance
- [Update CHANGELOG.md](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/fa7c671073cba4d511bc6bcf1beed5b3fe76bd91) - @RogerSelwyn
- [Bump to v0.10.6](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/9202ab59de10cf99c6db82891f789b172441c4e2) - @RogerSelwyn

## 0.10.5 (2023/01/04)
### Enhancements
- [Add mode/preset/temperature setting](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/71b967e2674fee43c99e135ad4424abac5dd3d7f) - @RogerSelwyn

### Maintenance
- [Segregate code to add clarity for adding climate](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/5a274b97c6b657f3be627f76d96f8a507996214f) - @RogerSelwyn
- [Bump to v0.10.5](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/bfa53600f170c347eaa5be201ea0b2637c932bd8) - @RogerSelwyn

## 0.10.4 (2023/01/04)
### Enhancements
- [Support friendly name](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/18cf6f1a94f5f72bb0e7b8dfbe0cc93c45e190ec) - @RogerSelwyn

### Maintenance
- [Convert strings to constants](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/eb83759ce944516aea33c3fd5d22c27859eae72f) - @RogerSelwyn
- [Bump to v0.10.4](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/0941c09b772a53c8a78de05b0d2d89d3a07a557c) - @RogerSelwyn

## 0.10.3 (2023/01/03)
### Maintenance
- [Code improvements](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/b7352e7338402148caabe7c07689ed99ab65e025) - @RogerSelwyn
- [Bump to v0.10.3](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/a9c439158bbb256197a7aa00c897693c7e84fc17) - @RogerSelwyn

## 0.10.2 (2022/12/29)
### Fixes
- [Fix subscription failure - retry in 10 seconds](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/53baa29c4e89673561c04c3a6dcdafab0ecb3d0b) - @RogerSelwyn

### Maintenance
- [Bring more in line with core statestream](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/edd54ec94f3aa846c533b491012568c0dba2d888) - @RogerSelwyn
- [Bump to 0.10.2](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/8943750da9e2e67457b1e31c8aa56a2aa03f705f) - @RogerSelwyn


## 0.10.1 (2022/12/28)
### Enhancements
- [Add icon as standard attribute](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/ae08fef9626c01c90b2fa61c59ced97750f354f0) - @RogerSelwyn

### Maintenance
- [Substantial re-organisation of code](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/8c1407ef6fbc8f6a6b1bcab72b0748260c116333) - @RogerSelwyn
- [Bump to  0.10.1](https://github.com/RogerSelwyn/mqtt_discoverystream_ha/commit/b19bc0d4ecb7a1c4c1806d5521e692a2a34abb5a) - @RogerSelwyn

## 0.10.0 (2022/12/24)
### Enhancements
- Added climate entity support

### Maintenance
- Workaround for MQTT failure at startup

## 0.9

- Fix `async_get_registry` warning

## 0.8

- Add "discovery_topic" to split config and state topics

## 0.7

- Fix availability for lights

## 0.6

- Adapt to 2021.12

## 0.5

- Add device support
- Fix color support
- Add availability support

## 0.4

- Add device_tracker
- Add light transitions
- Initial HACS release

## 0.3

- Manage color temperature

## 0.2

- Fix binary_sensors

## 0.1

- Initial release:
  Handles:
    - sensors
    - switches
    - lights (partial)
