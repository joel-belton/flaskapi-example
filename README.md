# API Documentation

## Chores
### Chore Details
- Identifier
- Name (Text)
- Description (Long text)
- Assignee (Select)
- Repeating (Int - number of weeks)
- Complete (boolean)
- Week Completed (Int - Week number)


## Usage

All Responses will have this form

```json
{
    "data" : "Mixed type holding the content of the response",
    "message" : "Description of waht happened"
}
```

### API Functionality

- List all chores
- Create Chore
- Get information on chore
- Update Chore
- Delete Chore

### List all Chores

**Definition**

` GET /chores`

**Response**

- `200 OK` on success

```json
[
    {
        "Identifier" : "bin",
        "name" : "Put Bins Out",
        "description" : "Put all bins outside every Tuesday",
        "Assignee" : "Joel",
        "Repeating" : "1",
        "Complete" : "False",
        "Week Completed" : "23"
    },
    {
        "Identifier" : "clean-kitchen",
        "name" : "Tidy Kitchen",
        "description" : "Deep clean of the kitchen and all surfaces",
        "Assignee" : "Chloe",
        "Repeating" : "4",
        "Complete" : "False",
        "Week Completed" : "21"
    }
]
```

### Get Information on Chore

**Definition**

` GET /chores/<Identifier>`

**Response**

- `200 OK` on success
- `404 NOT FOUND` when no chore is found with given Identifier

```json
{
    "Identifier" : "bin",
    "name" : "Put Bins Out",
    "description" : "Put all bins outside every Tuesday",
    "Assignee" : "Joel",
    "Repeating" : "1",
    "Complete" : "False"
}
```

### Create new Chore

**Definition**

` POST /chores/create`

**Arguments**

- `"name":string` a human readable name for this chore
- `"description":string` a longer description of what work has to be done
- `"repeating":int` Number of weeks until this should repeat again

**Response**

- `200 OK` on success

```json
{
    "Identifier" : "bin",
    "name" : "Put Bins Out",
    "description" : "Put all bins outside every Tuesday",
    "Assignee" : "Joel",
    "Repeating" : "1",
    "Complete" : "False"
}
```

###  Delete a Chore

**Definition**
`Delete /chores/<Identifier>/delete`

**Response**
- `200 OK` on success
- `204 No Content` on not found


### Update details about a chore

**Definition**

`POST /chores/<Identifier>/update`

**Arguments**

- `"name":string` a human readable name for this chore
- `"description":string` a longer description of what work has to be done
- `"repeating":int` Number of weeks until this should repeat again

**Response**

- `200 OK` on success

```json
{
    "Identifier" : "bin",
    "name" : "Put Bins Out",
    "description" : "Put all bins outside every Tuesday",
    "Assignee" : "Joel",
    "Repeating" : "1",
    "Complete" : "False"
}
```
