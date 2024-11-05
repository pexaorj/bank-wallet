# Bank Wallet Project - Microservices with Kubernetes

## Project Description

This project simulates a bank wallet using a microservices architecture with Kubernetes. The application enables user registration, login, and the management of credit and debit transactions. The wallet is designed to manage virtual money balances, secure transactions, and maintain logs for transaction tracking. The system employs Istio as a service mesh for secure and observable communication between services.

This project is intended for learning and practicing DevOps and SRE, with a focus on infrastructure automation, monitoring, and scalability using Kubernetes, Terraform, Docker, Helm, Kustomize, and ArgoCD.

## Requirements

- **Wallet Balance**: Each user has a balance stored in their wallet, which can be modified through API calls.
- **Transaction Management**: Supports increasing and decreasing balance via transactions, with logging for each transaction in a database or log.
- **Security**: Only authenticated users can initiate transactions.
- **Asynchronous Transactions**: Transactions are processed asynchronously for stability and reliability.
- **UUID Wallet Structure**: Wallets include a UUID, balance, User_ID, and Credit_Card_ID.
- **Transaction Monitoring**: Each transaction has a unique ID to allow monitoring across microservices.
- **Service Mesh**: Uses Istio for secure and managed communication between services.

## Tech Stack

- **Backend**: Python (Flask)
- **Orchestration**: Kubernetes with Istio as the service mesh
- **Infrastructure as Code**: Terraform
- **Containers**: Docker
- **Cache**: Redis
- **Database**: PostgreSQL
- **Message Queue**: RabbitMQ
- **Monitoring**: Prometheus and Grafana
- **Configuration Management**: Helm and Kustomize
- **Continuous Delivery**: ArgoCD

## Directory Structure

```
bank-wallet-project/
├── README.md
├── .gitignore
├── docker/
│   ├── Dockerfile.auth            # Dockerfile for authentication service
│   ├── Dockerfile.transactions     # Dockerfile for transactions service
│   ├── Dockerfile.balance          # Dockerfile for balance service
│   └── Dockerfile.web              # Dockerfile for web interface
├── kubernetes/
│   ├── auth-deployment.yaml        # Deployment configuration for authentication service
│   ├── transactions-deployment.yaml
│   ├── balance-deployment.yaml
│   ├── redis-deployment.yaml       # Redis configuration
│   ├── postgres-statefulset.yaml   # PostgreSQL StatefulSet configuration
│   ├── service.yaml                # Service to expose the application
│   ├── istio-gateway.yaml          # Istio gateway and virtual service configuration
│   └── configmap-secrets.yaml      # ConfigMap and Secrets
├── terraform/
│   ├── main.tf                     # Main Terraform configuration
│   ├── variables.tf                # Variables for the cluster and services
│   └── outputs.tf                  # Useful outputs like endpoints
├── services/
│   ├── auth/
│   │   ├── app.py                  # Authentication service code
│   │   └── db_config.py            # Configuration for PostgreSQL and Redis connection
│   ├── transactions/
│   │   └── app.py                  # Transactions service code
│   └── balance/
│       └── app.py                  # Balance service code
├── web/
│   └── app.py                      # Web interface code
├── monitoring/
│   ├── prometheus/
│   │   └── prometheus-config.yaml   # Prometheus configuration
│   └── grafana/
│       └── grafana-dashboard.json   # Grafana dashboard
└── requirements.txt                 # Python dependencies
```

## Service Descriptions

### 1. **Authentication Service**
- Responsible for registering and authenticating users.
- Uses PostgreSQL for user data storage and Redis for session caching.
  
### 2. **Transactions Service**
- Receives transaction requests (credit/debit) and queues them for processing asynchronously.
- Communicates with the balance service through RabbitMQ, logging each transaction in the database.

### 3. **Balance Service**
- Consumes messages from the RabbitMQ queue and updates user balances in PostgreSQL.
- Each transaction has a unique ID, allowing for monitoring and tracing of issues across services.

### 4. **Web Interface**
- A simple interface for user registration, login, and balance view.

### 5. **Istio Service Mesh**
- Manages service-to-service communication, enabling secure and observable connections across the microservices.

## Setup and Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/pexaorj/bank-wallet-project.git
   cd bank-wallet-project
   ```

2. **Build Docker Images**

   For each service (auth, transactions, balance, and web), go to the `docker/` directory and build the images:

   ```bash
   docker build -f Dockerfile.auth -t auth-service .
   docker build -f Dockerfile.transactions -t transactions-service .
   docker build -f Dockerfile.balance -t balance-service .
   docker build -f Dockerfile.web -t web-service .
   ```

3. **Kubernetes Setup**

   Apply the deployments, services, and Istio configurations in Kubernetes:

   ```bash
   kubectl apply -f kubernetes/
   ```

4. **Terraform Setup**

   Go to the `terraform/` directory, edit `variables.tf` as needed, and initialize the environment:

   ```bash
   terraform init
   terraform apply
   ```

5. **Monitoring**

   Set up Prometheus and Grafana using the configuration files in `monitoring/`.

6. **Management with Helm, Kustomize, and ArgoCD**

   To use Helm and Kustomize, you can set up ArgoCD to observe and automatically apply changes based on the manifests.

   ```bash
   # Install Helm charts and Kustomize overlays
   helm install auth helm/auth/
   kubectl apply -k kustomize/overlays/local/
   ```

---

This README now includes all the new project requirements. Adjust specific settings and details as necessary for your environment.