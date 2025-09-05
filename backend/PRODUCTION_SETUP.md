# Production Setup Guide

## Environment Variables for Production

Create a `.env` file in the backend directory with the following variables:

### Database Configuration
```env
DATABASE_URL=postgresql://username:password@localhost:5432/student_interview_app
```

### JWT Configuration
```env
JWT_SECRET=your-super-secret-jwt-key-here
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15
REFRESH_TOKEN_EXPIRE_DAYS=7
```

### Storage Configuration (MinIO/S3)
```env
STORAGE_ENDPOINT=http://localhost:9000
STORAGE_ACCESS_KEY=your-minio-access-key
STORAGE_SECRET_KEY=your-minio-secret-key
STORAGE_BUCKET=cvs
STORAGE_REGION=us-east-1
```

### Payment Configuration (Razorpay)
```env
PAYMENT_PROVIDER=razorpay
RAZORPAY_KEY=rzp_test_your_razorpay_key_here
RAZORPAY_SECRET=your_razorpay_secret_here
MERCHANT_UPI_ID=your-merchant@upi
COMPANY_NAME=InterviewCredits
```

### Application Configuration
```env
APP_ORIGIN=http://localhost:5173
SESSION_SECRET_KEY=your-session-secret-key
```

## Razorpay Setup

1. **Create Razorpay Account:**
   - Go to https://razorpay.com
   - Sign up for a business account
   - Complete KYC verification

2. **Get API Keys:**
   - Go to Settings → API Keys
   - Generate new key pair
   - Copy Key ID and Key Secret

3. **Configure Webhooks:**
   - Go to Settings → Webhooks
   - Add webhook URL: `https://yourdomain.com/api/v1/payments/webhook`
   - Select events: `payment.captured`, `payment.failed`

4. **Set UPI ID:**
   - Get your UPI ID from your bank
   - Add it to `MERCHANT_UPI_ID` in .env

## Installation

1. **Install Dependencies:**
```bash
pip install -r requirements.txt
```

2. **Run Database Migrations:**
```bash
alembic upgrade head
```

3. **Start Server:**
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Testing Production Setup

1. **Test Payment Order Creation:**
```bash
curl -X POST "http://localhost:8000/api/v1/payments/order" \
  -H "Authorization: Bearer YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"pack_id": 1}'
```

2. **Verify Real UPI Link:**
   - Check that UPI link contains your real UPI ID
   - Test payment flow with small amount

3. **Test Webhook:**
   - Use Razorpay's webhook testing tool
   - Verify signature validation works

## Security Checklist

- [ ] Use strong JWT secret
- [ ] Enable HTTPS in production
- [ ] Set up proper CORS origins
- [ ] Configure firewall rules
- [ ] Use environment variables (never hardcode secrets)
- [ ] Enable webhook signature verification
- [ ] Set up monitoring and logging




