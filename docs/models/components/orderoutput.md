# OrderOutput

An order to be returned


## Fields

| Field                                                                | Type                                                                 | Required                                                             | Description                                                          | Example                                                              |
| -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- | -------------------------------------------------------------------- |
| `id`                                                                 | *int*                                                                | :heavy_check_mark:                                                   | The id of the order                                                  | 1                                                                    |
| `burger_ids`                                                         | List[*int*]                                                          | :heavy_check_mark:                                                   | List of burger ids in the order                                      | 1,2                                                                  |
| `time`                                                               | [date](https://docs.python.org/3/library/datetime.html#date-objects) | :heavy_check_mark:                                                   | Time of the order                                                    | 2021-01-01T12:00:00                                                  |
| `table`                                                              | *int*                                                                | :heavy_check_mark:                                                   | Table number for the order                                           | 1                                                                    |
| `status`                                                             | [components.OrderStatus](../../models/components/orderstatus.md)     | :heavy_check_mark:                                                   | N/A                                                                  | CREATED                                                              |
| `note`                                                               | *Optional[str]*                                                      | :heavy_minus_sign:                                                   | Note for the order                                                   | No onions                                                            |