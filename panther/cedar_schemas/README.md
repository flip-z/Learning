### Custom Schema Directory Guide

1. Create a directory to store the custom schema files in. Name it after the specific log type that's being parsed (e.g. `jamf_ulogs/`).
2. Create your test files (e.g. `jamf_ulogs.yml` and `jamf_ulogs_tests.yml`) or parse files (e.g. `jamf_ulogs_example.jsonl`) with the same name.

_Documentation for creating custom schemas can be found here: https://docs.runpanther.io/data-onboarding/custom-log-types_

```
cedar_schemas/
│   README.md    
│
└───mycustomschema/
│   │   mycustomschema.yml
│   │   mycustomschema_tests.yml
|   |   mycustomschema_example.jsonl
```
