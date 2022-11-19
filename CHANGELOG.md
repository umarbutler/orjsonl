# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.1.3] - 2022-11-20

### Changed

- Removed unnecessary links to `load()`, `stream()`, `save()` and `append()` in the README file.

## [0.1.2] - 2022-11-20

### Added

- Allowed for the `default` and `option` arguments to be passed to `orjson.dumps()` through `save()` and `append()`.
- Added 'ndjson' as a keyword in the project metadata.

## [0.1.1] - 2022-11-19

### Added

- Created a changelog.
- Added 'lines', 'json lines' and 'fast' as keywords in the project metadata.

### Changed

- Renamed the 'Bug Tracker' url to 'Issues' in the project metadata.
- Specified orjsonl's license to be the MIT License in the project metadata.
- Fixed typos in the README file.
- Fixed typos in the tests script.

## [0.1.0] - 2022-11-18

### Added

- Added the `load()` function, which deserializes a UTF-8-encoded jsonl file to a list of Python objects.
- Added the `stream()` function, which creates a map object that deserializes a UTF-8-encoded jsonl file to Python objects.
- Added the `save()` function, which serializes an iterable of Python objects to a UTF-8-encoded jsonl file.
- Added the `append()` function, serializes and appends an iterable of Python objects to a UTF-8-encoded jsonl file.

[0.1.3]: https://github.com/umarbutler/orjsonl/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/umarbutler/orjsonl/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/umarbutler/orjsonl/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/umarbutler/orjsonl/releases/tag/v0.1.0
