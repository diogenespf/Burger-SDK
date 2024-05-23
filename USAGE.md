<!-- Start SDK Example Usage [usage] -->
```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers()


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass

```
<!-- End SDK Example Usage [usage] -->