# Python proto rules
Python protobuf definitions for the [Proto plugin](https://github.com/please-build/proto-rules), for the [Please](https://please.build) build system.

## Basic usage
First add the `proto` plugin and this plugin to your project:

```python
# BUILD
plugin_repo(
    name = "proto",
    revision = "<Some git tag, commit, or other reference>",
)

plugin_repo(
    name = "python_proto",
    revision = "<Some git tag, commit, or other reference>",
)
```

`proto_library` and `grpc_library` rules are now ready to be used in Python rules:

```python
grpc_library(
    name = "proto",
    srcs = ["service.proto"],
    visibility = ["//service/..."],
)
```

```python
python_binary(
    name = "service",
    main = "main.py",
    # This is the proto above
    deps = ["//service/proto:proto"],
)
```

> See [Proto plugin](https://github.com/please-build/proto-rules) and [Python plugin](https://github.com/please-build/python-rules) for more information and configuration options.


## Configuration

The available configuration options and defaults are:

```ini
[Plugin "python_proto"]
ProtoPlugin = grpc_python_plugin
ProtoDep = //third_party/python:protobuf
GrpcDep = //third_party/python:grpc
```
