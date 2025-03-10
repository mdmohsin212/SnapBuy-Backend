# **SnapBuy - Ultimate Online Shopping Destination**  

Discover **SnapBuy**, a cutting-edge e-commerce platform that makes online shopping easy and convenient. From browsing a diverse range of products to making secure payments and tracking your orders, SnapBuy ensures a seamless and enjoyable shopping journey.  
 

---

## **Features**  

### **User Authentication & Security**  
- **Account Creation**: Customers can register by providing their details and verifying their email before accessing their account.  
- **Secure Login System**: User authentication is handled using **JWT tokens**, ensuring a safe and persistent login session.  
- **Access Control**: Role-based permissions differentiate between customers and admins, providing appropriate access to platform functionalities.  

### **Customer Features**  
- **Browse & Discover Products**: Users can explore various product categories and find the items they need.  
- **Cart**: Customers can add products to their cart for easy checkout.  
- **Seamless Payment**: Transactions are securely processed through **SSLCommerz**, ensuring a safe buying experience.  
- **Order Status & Tracking**: After making a purchase, customers can monitor their order’s progress in real-time.  

### **Admin Features**  
- **Order Processing**: Admins have the ability to update order statuses, including shipping and delivery updates.  
- **Analytics & Reports**: A dashboard provides an overview of customer activities, orders, and sales performance.  
- **Product Inventory Management**: Admins can add new products, update existing listings, and remove items as needed.  


---
## **Technology Stack**  
<div style="display: flex; gap: 10px;">
  <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white" alt="Django">
  <img src="https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL (Supabase)">
  <img src="https://img.shields.io/badge/JWT-000000?style=for-the-badge&logo=jsonwebtokens&logoColor=white" alt="JWT Authentication">
  <img src="https://img.shields.io/badge/Vercel-000000?style=for-the-badge&logo=vercel&logoColor=white" alt="Vercel">
  <img src="https://img.shields.io/badge/Cloudinary-3448C5?style=for-the-badge&logo=cloudinary&logoColor=white" alt="Cloudinary">
</div>

---

## **Installation & Setup**  

1. **Clone the repository**  
    ```bash
   git clone https://github.com/mdmohsin212/SnapBuy-Backend.git
    ```
2. **Install dependencies**
    ```
    cd SnapBuy-Backend
    ```
3. **Environment Configuration**
    Create a .env file and set up the required credentials

4. **Run Database Migrations**
    ```
    python manage.py migrate
    ```
5. **Start the Server**
    ```
    python manage.py runserver
    ```

## **API Endpoints**  

### **Authentication**  
- `https://snap-buy-backend.vercel.app/user/register/` → Register new users (Customers & Admins)  
- `https://snap-buy-backend.vercel.app/user/login/` → Authenticate users and return a JWT token  
- `https://snap-buy-backend.vercel.app/user/profile/` → Retrieve user profile details  
- `https://snap-buy-backend.vercel.app/user/logout/` → Log out the user  
- `https://snap-buy-backend.vercel.app/user/contact/` → Submit user contact information  

### **Product Management**  
- `https://snap-buy-backend.vercel.app/product/list/` → Retrieve all available products  
- `https://snap-buy-backend.vercel.app/product/category/` → Retrieve product categories  
- `https://snap-buy-backend.vercel.app/product/cart/` → Retrieve cart items  
- `https://snap-buy-backend.vercel.app/product/review/` → Retrieve product reviews  

### **Payment**  
- `https://snap-buy-backend.vercel.app/payment/make_payment/?id=<user_id>/` → Process payment for a specific user  
- `https://snap-buy-backend.vercel.app/payment/checkout/` → Handle the checkout process  
- `https://snap-buy-backend.vercel.app/payment/orderitem/` → Retrieve order details  

### **User Profiles**  
- `https://snap-buy-backend.vercel.app/user/profile/?id=<user_id>` → Retrieve a specific user profile  
 


## **Live Deployment**  

- **Backend API**: Hosted on Vercel  
- **Frontend Application**: [SnapBuy Frontend](https://snapbuy-frontend.vercel.app/)  

---

## **Authentication Workflow**  

1. **User Sign-Up**: Registration request is submitted → Email confirmation is sent.  
2. **Email Verification**: User confirms email → Account gets activated.  
3. **JWT Login**: User logs in → JWT token is generated & stored for session management.  
4. **Secure Access**: User accesses platform features based on role (Customers/ Admin).  