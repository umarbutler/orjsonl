# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.2] - 2022-12-24

### Fixed

- Updated the link to the GitHub Actions shield as per badges/shields#8671.

## [0.2.1] - 2022-11-23

### Added

- Added new keywords to the project metadata.

### Changed

- Rephrased and simplifed the README file.
- Changed the order of `stream()` and `load()` in `orjsonl.py`.

### Fixed

- Corrected typos in the README file.
- Corrected typos in the changelog.
- Corrected typos in docstrings.

## [0.2.0] - 2022-11-22

### Added

- Added support for gzip, bzip2, xz and Zstandard compression to `load()`, `stream()`, `save()` and `append()` as requested in [#1](https://github.com/umarbutler/orjsonl/issues/1).
- Created `py.typed`.
- Ensured that `load()`, `stream()`, `save()` and `append()` are tested with compressed jsonl files.

### Changed

- Changed `stream()` to return a `generator` rather than a `map`.
- Changed `load()`, `stream()`, `save()` and `append()` to rely on [`xopen.xopen()`](https://github.com/pycompression/xopen/#xopen) rather than [`open()`](https://docs.python.org/3/library/functions.html#open).
- Updated the package description and README file to reflect the fact that `orjsonl` now supports compression.

### Fixed

- Fixed [#1](https://github.com/umarbutler/orjsonl/issues/1) by ensuring that `stream()` closes jsonl files whenever a `generator` has been exhuasted.
- Corrected typos in the changelog.
- Corrected typos in docstrings.
- Ensured that optional arguments are type hinted as such.
- Updated dependencies to prevent the use of versions of [`orjson`](https://github.com/ijl/orjson) older than 3.7.7.

### Removed

- Removed support for integer file descriptors.

## [0.1.3] - 2022-11-20

### Removed

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
- Specified `orjsonl`'s license to be the MIT License in the project metadata.

### Fixed

- Fixed typos in the README file.
- Fixed typos in the tests script.

## [0.1.0] - 2022-11-18

### Added

- Added the `load()` function, which deserializes a UTF-8-encoded jsonl file to a list of Python objects.
- Added the `stream()` function, which creates a map object that deserializes a UTF-8-encoded jsonl file to Python objects.
- Added the `save()` function, which serializes an iterable of Python objects to a UTF-8-encoded jsonl file.
- Added the `append()` function, serializes and appends an iterable of Python objects to a UTF-8-encoded jsonl file.

[0.2.2]: https://github.com/umarbutler/orjsonl/compare/v0.2.1...v0.2.2
[0.2.1]: https://github.com/umarbutler/orjsonl/compare/v0.2.0...v0.2.1
[0.2.0]: https://github.com/umarbutler/orjsonl/compare/v0.1.3...v0.2.0
[0.1.3]: https://github.com/umarbutler/orjsonl/compare/v0.1.2...v0.1.3
[0.1.2]: https://github.com/umarbutler/orjsonl/compare/v0.1.1...v0.1.2
[0.1.1]: https://github.com/umarbutler/orjsonl/compare/v0.1.0...v0.1.1
[0.1.0]: https://github.com/umarbutler/orjsonl/releases/tag/v0.1.0
