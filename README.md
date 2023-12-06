# APItizing-Burgers

<div align="left">
    <a href="https://speakeasyapi.dev/"><img src="https://custom-icon-badges.demolab.com/badge/-Built%20By%20Speakeasy-212015?style=for-the-badge&logoColor=FBE331&logo=speakeasy&labelColor=545454" /></a>
    <a href="https://github.com/diogenespf/Burger-SDK.git/actions"><img src="https://img.shields.io/github/actions/workflow/status/diogenespf/Burger-SDK/speakeasy_sdk_generation.yml?style=for-the-badge" /></a>
    
</div>


## 🏗 **Welcome to your new SDK!** 🏗

It has been generated successfully based on your OpenAPI spec. However, it is not yet ready for production use. Here are some next steps:
- [ ] 🛠 Make your SDK feel handcrafted by [customizing it](https://www.speakeasyapi.dev/docs/customize-sdks)
- [ ] ♻️ Refine your SDK quickly by iterating locally with the [Speakeasy CLI](https://github.com/speakeasy-api/speakeasy)
- [ ] 🎁 Publish your SDK to package managers by [configuring automatic publishing](https://www.speakeasyapi.dev/docs/productionize-sdks/publish-sdks)
- [ ] ✨ When ready to productionize, delete this section from the README
<!-- Start SDK Installation [installation] -->
## SDK Installation

```bash
pip install git+https://github.com/diogenespf/Burger-SDK.git
```
<!-- End SDK Installation [installation] -->

<!-- Start SDK Example Usage [usage] -->
## SDK Example Usage

### Example

```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers()


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass
```
<!-- End SDK Example Usage [usage] -->

<!-- Start Available Resources and Operations [operations] -->
## Available Resources and Operations

### [burger](docs/sdks/burger/README.md)

* [list_burgers](docs/sdks/burger/README.md#list_burgers) - List Burgers
* [create_burger](docs/sdks/burger/README.md#create_burger) - Create Burger
* [delete_burger](docs/sdks/burger/README.md#delete_burger) - Delete Burger
* [read_burger](docs/sdks/burger/README.md#read_burger) - Read Burger
* [update_burger](docs/sdks/burger/README.md#update_burger) - Update Burger

### [order](docs/sdks/order/README.md)

* [list_orders](docs/sdks/order/README.md#list_orders) - List Orders
* [create_order](docs/sdks/order/README.md#create_order) - Create Order
* [read_order](docs/sdks/order/README.md#read_order) - Read Order
* [update_order](docs/sdks/order/README.md#update_order) - Update Order
<!-- End Available Resources and Operations [operations] -->

<!-- Start Retries [retries] -->
## Retries

Some of the endpoints in this SDK support retries.  If you use the SDK without any configuration, it will fall back to the default retry strategy provided by the API.  However, the default retry strategy can be overridden on a per-operation basis, or across the entire SDK.

To change the default retry strategy for a single API call, simply provide a retryConfig object to the call:
```python
import apitizing_burgers
from apitizing_burgers.utils import BackoffStrategy, RetryConfig

s = apitizing_burgers.APItizingBurgers()


res = s.burger.list_burgers(,
    RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False))

if res.response_listburgers is not None:
    # handle response
    pass
```

If you'd like to override the default retry strategy for all operations that support retries, you can provide a retryConfig at SDK initialization:
```python
import apitizing_burgers
from apitizing_burgers.utils import BackoffStrategy, RetryConfig

s = apitizing_burgers.APItizingBurgers(
    retry_config=RetryConfig('backoff', BackoffStrategy(1, 50, 1.1, 100), False)
)


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass
```
<!-- End Retries [retries] -->

<!-- Start Error Handling [errors] -->
## Error Handling

Handling errors in this SDK should largely match your expectations.  All operations return a response object or raise an error.  If Error objects are specified in your OpenAPI Spec, the SDK will raise the appropriate Error type.

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| errors.HTTPValidationError | 422                        | application/json           |
| errors.SDKError            | 400-600                    | */*                        |

### Example

```python
import apitizing_burgers
from apitizing_burgers.models import components

s = apitizing_burgers.APItizingBurgers()

req = components.BurgerCreate(
    name='Cheeseburger',
    description='Veggie burger with avocado',
)

res = None
try:
    res = s.burger.create_burger(req)
except errors.HTTPValidationError as e:
    print(e)  # handle exception
    raise(e)
except errors.SDKError as e:
    print(e)  # handle exception
    raise(e)

if res.burger_output is not None:
    # handle response
    pass
```
<!-- End Error Handling [errors] -->

<!-- Start Server Selection [server] -->
## Server Selection

### Select Server by Index

You can override the default server globally by passing a server index to the `server_idx: int` optional parameter when initializing the SDK client instance. The selected server will then be used as the default on the operations that use it. This table lists the indexes associated with the available servers:

| # | Server | Variables |
| - | ------ | --------- |
| 0 | `http://127.0.0.1:8000/` | None |

#### Example

```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers(
    server_idx=0,
)


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass
```


### Override Server URL Per-Client

The default server can also be overridden globally by passing a URL to the `server_url: str` optional parameter when initializing the SDK client instance. For example:
```python
import apitizing_burgers

s = apitizing_burgers.APItizingBurgers(
    server_url="http://127.0.0.1:8000/",
)


res = s.burger.list_burgers()

if res.response_listburgers is not None:
    # handle response
    pass
```
<!-- End Server Selection [server] -->

<!-- Start Custom HTTP Client [http-client] -->
## Custom HTTP Client

The Python SDK makes API calls using the (requests)[https://pypi.org/project/requests/] HTTP library.  In order to provide a convenient way to configure timeouts, cookies, proxies, custom headers, and other low-level configuration, you can initialize the SDK client with a custom `requests.Session` object.

For example, you could specify a header for every request that this sdk makes as follows:
```python
import apitizing_burgers
import requests

http_client = requests.Session()
http_client.headers.update({'x-custom-header': 'someValue'})
s = apitizing_burgers.APItizingBurgers(client: http_client)
```
<!-- End Custom HTTP Client [http-client] -->

<!-- Placeholder for Future Speakeasy SDK Sections -->

# Development

## Maturity

This SDK is in beta, and there may be breaking changes between versions without a major version update. Therefore, we recommend pinning usage
to a specific package version. This way, you can install the same version each time without breaking changes unless you are intentionally
looking for the latest version.

## Contributions

While we value open-source contributions to this SDK, this library is generated programmatically.
Feel free to open a PR or a Github issue as a proof of concept and we'll do our best to include it in a future release!

### SDK Created by [Speakeasy](https://docs.speakeasyapi.dev/docs/using-speakeasy/client-sdks)
