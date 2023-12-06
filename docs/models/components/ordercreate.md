# OrderCreate

Fields to create an order


## Fields

| Field                           | Type                            | Required                        | Description                     | Example                         |
| ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- | ------------------------------- |
| `burger_ids`                    | List[*int*]                     | :heavy_check_mark:              | List of burger ids in the order | [1,2]                           |
| `table`                         | *int*                           | :heavy_check_mark:              | Table number for the order      | 1                               |
| `note`                          | *Optional[str]*                 | :heavy_minus_sign:              | Note for the order              | No onions                       |