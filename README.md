# E-commerce Management Service

A comprehensive Python-based service to manage products, analyze niches, track orders, perform smart analytics and predictions, manage promotions, handle user profiles, and more across multiple e-commerce platforms 

## Structure

ecommerce_service/
├── main.py
├── models.py
├── schemas.py
├── database.py
├── dependencies.py
├── services/
│   ├── __init__.py
│   ├── avito.py
│   ├── ozon.py
│   ├── wildberries.py
│   └── yandex.py
├── analytics/
│   ├── __init__.py
│   ├── abc_analysis.py
│   ├── order_analysis.py
│   ├── predictions.py
│   ├── profit_analysis.py
│   └── xyz_analysis.py
├── dashboards/
│   └── dashboard.py
├── users/
│   ├── __init__.py
│   ├── auth.py
│   ├── profile.py
│   └── favorites.py
├── niche/
│   ├── __init__.py
│   ├── search.py
│   └── analysis.py
├── promotion/
│   ├── __init__.py
│   ├── seo.py
│   ├── keywords.py
│   ├── semantic_collection.py
│   ├── position_tracking.py
│   ├── description_creation.py
│   ├── internal_advertising.py
│   ├── rates.py
│   └── ad_management.py
├── management/
│   ├── __init__.py
│   ├── price_management.py
│   ├── auto_replies.py
│   └── hypothesis_testing.py
├── notifications/
│   ├── __init__.py
│   └── notifications.py
├── calendar/
│   ├── __init__.py
│   └── calendar.py
├── suppliers/
│   ├── __init__.py
│   ├── catalog.py
│   └── china_suppliers.py
├── categories/
│   ├── __init__.py
│   └── categories.py
├── sellers/
│   ├── __init__.py
│   └── sellers.py
├── brands/
│   ├── __init__.py
│   └── brands.py
├── tariffs/
│   ├── __init__.py
│   └── tariffs.py
├── search/
│   ├── __init__.py
│   └── search.py
├── premium/
│   ├── __init__.py
│   └── premium.py
├── requirements.txt
└── README.md

## Setup Instructions

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/ecommerce_service.git
    cd ecommerce_service
    ```

2. **Create a Virtual Environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configure Environment Variables**

    - Create a `.env` file in the root directory with the following content:

        ```env
        API_KEY=YOUR_SECURE_API_KEY
        SECRET_KEY=YOUR_JWT_SECRET_KEY
        WILDBERRIES_API_TOKEN=YOUR_WILDBERRIES_API_TOKEN
        OZON_CLIENT_ID=YOUR_OZON_CLIENT_ID
        OZON_API_KEY=YOUR_OZON_API_KEY
        YANDEX_OAUTH_TOKEN=YOUR_YANDEX_OAUTH_TOKEN
        YOUR_CAMPAIGN_ID=YOUR_CAMPAIGN_ID
        AVITO_CLIENT_ID=YOUR_AVITO_CLIENT_ID
        AVITO_CLIENT_SECRET=YOUR_AVITO_CLIENT_SECRET
        ```

5. **Run the Application**

    ```bash
    python main.py
    ```

    - The application will start and provide a public URL via ngrok. Use this URL to access the API endpoints.

## API Endpoints

### **Authentication**

- **Register a New User**

    - **URL**: `/auth/register`
    - **Method**: `POST`
    - **Body**:

        ```json
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```

- **Login**

    - **URL**: `/auth/login`
    - **Method**: `POST`
    - **Body**:

        ```json
        {
            "username": "your_username",
            "password": "your_password"
        }
        ```

    - **Response**:

        ```json
        {
            "access_token": "jwt_token",
            "token_type": "bearer"
        }
        ```

### **User Profile**

- **Get Profile**

    - **URL**: `/profile/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Update Profile**

    - **URL**: `/profile/`
    - **Method**: `PUT`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "id": 1,
            "username": "new_username"
        }
        ```

### **Favorites**

- **Add to Favorites**

    - **URL**: `/favorites/{product_id}`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **List Favorites**

    - **URL**: `/favorites/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Remove from Favorites**

    - **URL**: `/favorites/{product_id}`
    - **Method**: `DELETE`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Niche Management**

- **Analyze Niches**

    - **URL**: `/niche/analyze`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Search Niches**

    - **URL**: `/niche/search?search_term=YOUR_TERM`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Categories**

- **Add Category**

    - **URL**: `/categories/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "name": "Electronics",
            "description": "All electronic items"
        }
        ```

- **List Categories**

    - **URL**: `/categories/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Get Category by ID**

    - **URL**: `/categories/{category_id}`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Sellers**

- **Add Seller**

    - **URL**: `/sellers/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "name": "BestSeller",
            "contact_info": "contact@bestseller.com"
        }
        ```

- **List Sellers**

    - **URL**: `/sellers/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Get Seller by ID**

    - **URL**: `/sellers/{seller_id}`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Brands**

- **Add Brand**

    - **URL**: `/brands/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "name": "BrandX",
            "description": "High-quality electronics"
        }
        ```

- **List Brands**

    - **URL**: `/brands/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Get Brand by ID**

    - **URL**: `/brands/{brand_id}`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Purchases**

- **Add Purchase**

    - **URL**: `/purchases/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "product_id": 1,
            "supplier_id": 2,
            "quantity": 100,
            "cost": 500.00
        }
        ```

- **List Purchases**

    - **URL**: `/purchases/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Get Purchase by ID**

    - **URL**: `/purchases/{purchase_id}`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Supplier Catalog**

Implement similar CRUD operations for Supplier Catalog as done for Categories, Sellers, and Brands.

### **Promotion Management**

- **SEO Optimization**

    - **URL**: `/promotion/seo/optimize`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "product_id": 1,
            "keywords": ["electronics", "smartphone"]
        }
        ```

- **Keywords Management**

    - **Add Keywords**

        - **URL**: `/promotion/keywords`
        - **Method**: `POST`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`
        - **Body**:

            ```json
            [
                {
                    "word": "smartphone"
                },
                {
                    "word": "electronics"
                }
            ]
            ```

    - **List Keywords**

        - **URL**: `/promotion/keywords`
        - **Method**: `GET`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`

    - **Delete Keyword**

        - **URL**: `/promotion/keywords/{keyword_id}`
        - **Method**: `DELETE`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`

### **Management Tools**

- **Price Management**

    - **URL**: `/management/price`
    - **Method**: `PUT`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "product_id": 1,
            "new_price": 1500.00
        }
        ```

- **Auto Replies**

    - **Add Auto Reply**

        - **URL**: `/management/auto-replies`
        - **Method**: `POST`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`
        - **Body**:

            ```json
            {
                "trigger": "order_received",
                "response": "Thank you for your order!"
            }
            ```

    - **List Auto Replies**

        - **URL**: `/management/auto-replies`
        - **Method**: `GET`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`

    - **Update Auto Reply**

        - **URL**: `/management/auto-replies/{auto_reply_id}`
        - **Method**: `PUT`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`
        - **Body**:

            ```json
            {
                "trigger": "order_shipped",
                "response": "Your order has been shipped!"
            }
            ```

    - **Delete Auto Reply**

        - **URL**: `/management/auto-replies/{auto_reply_id}`
        - **Method**: `DELETE`
        - **Headers**:
            - `Authorization`: `Bearer jwt_token`

- **Hypothesis Testing**

    Implement similar CRUD operations for hypothesis testing based on your requirements.

### **Notifications**

- **Send Notification**

    - **URL**: `/notifications/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "user_id": 1,
            "message": "Your order has been shipped.",
            "read": 0
        }
        ```

- **List Notifications**

    - **URL**: `/notifications/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Mark Notification as Read**

    - **URL**: `/notifications/{notification_id}/read`
    - **Method**: `PUT`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Calendar**

- **Add Event**

    - **URL**: `/calendar/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "user_id": 1,
            "title": "Product Launch",
            "description": "Launching the new smartphone model.",
            "start_time": "2024-12-01T10:00:00Z",
            "end_time": "2024-12-01T12:00:00Z"
        }
        ```

- **List Events**

    - **URL**: `/calendar/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Update Event**

    - **URL**: `/calendar/{event_id}`
    - **Method**: `PUT`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "user_id": 1,
            "title": "Updated Product Launch",
            "description": "Launching the updated smartphone model.",
            "start_time": "2024-12-02T10:00:00Z",
            "end_time": "2024-12-02T12:00:00Z"
        }
        ```

- **Delete Event**

    - **URL**: `/calendar/{event_id}`
    - **Method**: `DELETE`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

### **Tariffs and Premium Features**

- **Subscribe to Tariff**

    - **URL**: `/user_tariffs/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "tariff_id": 1,
            "end_date": "2025-12-31T23:59:59Z"
        }
        ```

- **List User Subscriptions**

    - **URL**: `/user_tariffs/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **List Tariffs**

    - **URL**: `/tariffs/`
    - **Method**: `GET`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`

- **Add Tariff**

    - **URL**: `/tariffs/`
    - **Method**: `POST`
    - **Headers**:
        - `Authorization`: `Bearer jwt_token`
    - **Body**:

        ```json
        {
            "name": "Premium",
            "price": 49.99,
            "features": "Unlimited access to all features."
        }
        ```


