# tcr_test
TestCommitRevert Test

- Install Save and Run
- Add the following to the settings
```    "saveAndRun": {
        "commands": [
            {
              "match": ".py$",
              "cmd": " (python ${file} && git commit -am working ) || git reset --hard HEAD",
              "useShortcut": false,
              "silent": false
            },
        ]
    },
```
