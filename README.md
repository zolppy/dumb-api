# Dumb API

A RESTful API for managing "dumbs" - simple string-based resources with unique identifiers.

## Base URL
```
http://localhost:8000
```

## API Endpoints

### Get All Dumbs
- **URL:** `/api/v1/dumbs/`
- **Method:** `GET`
- **Summary:** Retrieve all dumbs
- **Response:** 
  - **200 OK** - Returns an array of all dumbs
  ```json
  [
    {
      "string": "example string",
      "id": 1
    }
  ]
  ```

### Create a Dumb
- **URL:** `/api/v1/dumbs/`
- **Method:** `POST`
- **Summary:** Create a new dumb
- **Request Body:**
  ```json
  {
    "string": "example string"
  }
  ```
- **Response:**
  - **200 OK** - Returns the created dumb with ID
  ```json
  {
    "string": "example string",
    "id": 1
  }
  ```
  - **422 Validation Error** - Invalid input data

### Get Dumb by ID
- **URL:** `/api/v1/dumbs/{dumb_id}`
- **Method:** `GET`
- **Summary:** Retrieve a specific dumb by its ID
- **Parameters:**
  - `dumb_id` (integer, path parameter) - The ID of the dumb to retrieve
- **Response:**
  - **200 OK** - Returns the requested dumb
  ```json
  {
    "string": "example string",
    "id": 1
  }
  ```
  - **422 Validation Error** - Invalid ID format

### Delete Dumb by ID
- **URL:** `/api/v1/dumbs/{dumb_id}`
- **Method:** `DELETE`
- **Summary:** Delete a specific dumb by its ID
- **Parameters:**
  - `dumb_id` (integer, path parameter) - The ID of the dumb to delete
- **Response:**
  - **200 OK** - Returns the deleted dumb
  ```json
  {
    "string": "example string",
    "id": 1
  }
  ```
  - **422 Validation Error** - Invalid ID format

## Data Models

### DumbCreate
Represents a complete dumb object with both string content and ID.
```json
{
  "string": "string",
  "id": 0
}
```

### DumbIn
Represents input data for creating a new dumb (ID is generated server-side).
```json
{
  "string": "string"
}
```

### HTTPValidationError
Error response for validation failures.
```json
{
  "detail": [
    {
      "loc": ["string", 0],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

## Usage Examples

### Get all dumbs
```bash
curl -X GET "http://localhost:8000/api/v1/dumbs/"
```

### Create a new dumb
```bash
curl -X POST "http://localhost:8000/api/v1/dumbs/" \
  -H "Content-Type: application/json" \
  -d '{"string": "My new dumb"}'
```

### Get a specific dumb
```bash
curl -X GET "http://localhost:8000/api/v1/dumbs/1"
```

### Delete a dumb
```bash
curl -X DELETE "http://localhost:8000/api/v1/dumbs/1"
```

## Error Handling

The API returns standard HTTP status codes:
- `200` - Success
- `422` - Validation error (invalid input data or parameters)

For validation errors, the response includes detailed information about which fields failed validation and why.