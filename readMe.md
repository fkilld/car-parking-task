api to create car entry in parking

read car entries in parking
update car entries to show it left parking with time but entry time and exit time and then we want to calculate the total time spent in parking and here i want to car details like car number, entry time, exit time, total time spent in parking

delete car entries

---



## **📌 Car Parking API Documentation**

**Base URL:**

```
http://127.0.0.1:8000/api/carparkingdetails/
```

---

### **1️⃣ Get All Car Parking Entries**

**URL:**

```
GET /api/carparkingdetails/
```

**Method:** `GET`

**Description:**

* Fetches a list of all  **car parking entries** .
* Includes details like `car_number`, `car_name`, `inTime`, `outTime`, and `totalSpendTime`.

**Response Example:**

```json
[
    {
        "id": 1,
        "car_number": "MH352228",
        "car_name": "Eco Sport",
        "inTime": "2025-02-24T11:28:29.946121Z",
        "outTime": "2025-02-24T12:28:29.946145Z",
        "totalSpendTime": 60.0
    }
]
```

---

### **2️⃣ Get a Specific Car Parking Entry**

**URL:**

```
GET /api/carparkingdetails/{id}/
```

**Method:** `GET`

**Description:**

* Fetches **a specific car parking entry** by its ID.

**Example Request:**

```
GET /api/carparkingdetails/1/
```

**Response Example:**

```json
{
    "id": 1,
    "car_number": "MH352228",
    "car_name": "Eco Sport",
    "inTime": "2025-02-24T11:28:29.946121Z",
    "outTime": "2025-02-24T12:28:29.946145Z",
    "totalSpendTime": 60.0
}
```

---

### **3️⃣ Add a New Car Parking Entry**

**URL:**

```
POST /api/carparkingdetails/
```

**Method:** `POST`

**Description:**

* Adds a **new car entry** when a vehicle enters the parking lot.
* `inTime` is  **automatically set** .

**Request Body Example:**

```json
{
    "car_number": "MH999999",
    "car_name": "Honda City"
}
```

**Response Example:**

```json
{
    "id": 2,
    "car_number": "MH999999",
    "car_name": "Honda City",
    "inTime": "2025-02-24T14:00:00Z",
    "outTime": null,
    "totalSpendTime": null
}
```

✅ The **`inTime` is set automatically** when the car enters.

---

### **4️⃣ Update Car Exit Time & Calculate Total Parking Time**

**URL:**

```
PATCH /api/carparkingdetails/{id}/
```

**Method:** `PATCH`

**Description:**

* Updates `outTime` when a car **leaves** the parking.
* **Automatically calculates** `totalSpendTime`.

**Example Request:**

```
PATCH /api/carparkingdetails/1/
```

**Request Body:**

```json
{
    "outTime": "2025-02-24T14:30:00Z"
}
```

**Possible Responses:**

1. ✅ **Success:**

   ```json
   {
       "id": 1,
       "car_number": "MH352228",
       "car_name": "Eco Sport",
       "inTime": "2025-02-24T11:28:29.946121Z",
       "outTime": "2025-02-24T14:30:00Z",
       "totalSpendTime": 182.0
   }
   ```

   👉 **Total time is updated automatically.**
2. ❌ **Error (if `outTime` is before `inTime`):**

   ```json
   {
       "error": "outTime cannot be earlier than inTime"
   }
   ```

   👉 **System prevents negative time calculations.**

---

### **5️⃣ Delete a Car Parking Entry**

**URL:**

```
DELETE /api/carparkingdetails/{id}/
```

**Method:** `DELETE`

**Description:**

* **Removes** a car entry from the parking system.
* Cannot be undone.

**Example Request:**

```
DELETE /api/carparkingdetails/1/
```

**Response:** `204 No Content`

✅ Entry is  **successfully deleted** .

---

## **🚀 Summary of API Methods**

| **Action**               | **Method** | **URL**                    | **Description**                           |
| ------------------------------ | ---------------- | -------------------------------- | ----------------------------------------------- |
| **Get All Car Entries**  | `GET`          | `/api/carparkingdetails/`      | Retrieve all parking entries                    |
| **Get a Specific Entry** | `GET`          | `/api/carparkingdetails/{id}/` | Retrieve details of a specific parking entry    |
| **Create a New Entry**   | `POST`         | `/api/carparkingdetails/`      | Add a new car entry                             |
| **Update Exit Time**     | `PATCH`        | `/api/carparkingdetails/{id}/` | Set `outTime`and calculate `totalSpendTime` |
| **Delete an Entry**      | `DELETE`       | `/api/carparkingdetails/{id}/` | Remove a car entry                              |

Now, your **API documentation** is complete, simple, and professional! 🚀🔥
