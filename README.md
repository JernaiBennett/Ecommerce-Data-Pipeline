# E-Commerce Data Pipeline

A production-ready, end-to-end data engineering pipeline that processes e-commerce data using modern cloud technologies and workflow orchestration.

## 🎯 Project Overview

Built a scalable ETL pipeline that ingests, transforms, and analyzes e-commerce datasets (customers, products, orders, reviews) with automated workflow orchestration and containerized deployment.

## 🛠️ Technologies Used

- **Python 3.12** - Core programming language
- **AWS S3** - Cloud data lake storage
- **Prefect 3.x** - Workflow orchestration and monitoring
- **Docker & Docker Compose** - Containerization and deployment
- **Pandas** - Data transformation and analysis
- **boto3** - AWS SDK for Python

## 📊 Architecture
```
Raw Data (CSV) → S3 Upload → ETL Processing → Business Metrics → S3 Storage
                              ↓
                         Prefect Orchestration
                              ↓
                         Docker Containers
```

## ✨ Key Features

### 1. **Data Ingestion**
- Automated upload of multiple CSV files to AWS S3
- Date-partitioned data lake structure
- Support for multiple file formats (CSV, Parquet)

### 2. **ETL Pipeline**
- Data extraction from S3 buckets
- Data cleaning and validation
- Schema standardization
- Business metric calculations:
  - Customer segmentation analysis
  - Product performance metrics
  - Sales revenue aggregations

### 3. **Workflow Orchestration**
- Prefect flows for pipeline automation
- Task dependency management
- Automatic retries and error handling
- Real-time monitoring dashboard

### 4. **Containerization**
- Docker containerization for consistent environments
- Docker Compose for multi-service orchestration
- Production-ready deployment configuration

## 🚀 What I Learned

- **Cloud Data Engineering**: Implemented scalable data lake architecture on AWS S3
- **ETL Development**: Built robust Extract-Transform-Load pipelines with error handling
- **Workflow Orchestration**: Automated data pipelines using Prefect with scheduling and monitoring
- **Containerization**: Deployed applications using Docker for environment consistency
- **Data Modeling**: Designed data schemas and business metrics for analytics

## 📁 Project Structure
```
ecommerce-data-pipeline/
├── data/
│   └── raw/                    # Sample CSV datasets
├── data-pipeline/
│   ├── src/
│   │   ├── data_ingestion/     # S3 upload scripts
│   │   ├── data_processing/    # ETL transformations
│   │   └── orchestration/      # Prefect workflows
│   ├── config/                 # Configuration files
│   ├── tests/                  # Test scripts
│   ├── requirements.txt        # Python dependencies
│   └── docker-compose.yml      # Container orchestration
└── README.md
```

## 💻 Setup & Execution

### Prerequisites
- Python 3.10+
- AWS Account with S3 access
- Docker Desktop
- AWS credentials configured

### Quick Start

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/ecommerce-data-pipeline.git
cd ecommerce-data-pipeline
```

2. **Set up environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r data-pipeline/requirements.txt
```

3. **Configure AWS credentials**
Create `.env` file with:
```env
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_DEFAULT_REGION=us-east-1
AWS_S3_BUCKET_NAME=your-bucket-name
```

4. **Run the pipeline**
```bash
# Upload data to S3
python data-pipeline/src/data_ingestion/s3_uploader.py

# Process data
python data-pipeline/src/data_processing/etl_processor.py

# Run orchestrated workflow
python data-pipeline/src/orchestration/prefect_flows.py
```

5. **Run with Docker**
```bash
docker-compose -f data-pipeline/docker-compose.yml up --build
```

6. **Access Prefect UI**
Open http://localhost:4200 to monitor pipeline execution

## 📈 Pipeline Outputs

- **Cleaned datasets** stored in S3
- **Business metrics**: Customer lifetime value, product rankings, revenue trends
- **Automated monitoring** through Prefect dashboard
- **Execution logs** for debugging and optimization

## 🔍 Sample Datasets

| Dataset | Records | Description |
|---------|---------|-------------|
| customers.csv | 1,000+ | Customer demographics and profiles |
| products.csv | 500+ | Product catalog with pricing |
| orders.csv | 2,000+ | Order transactions |
| order_items.csv | 6,000+ | Line items per order |
| reviews.csv | 1,500+ | Customer reviews and ratings |

## 🎓 Skills Demonstrated

- **Data Engineering**: ETL pipeline design and implementation
- **Cloud Computing**: AWS S3 data lake architecture
- **Python Programming**: Data processing with Pandas, boto3
- **DevOps**: Docker containerization and deployment
- **Workflow Management**: Prefect orchestration and monitoring
- **Data Quality**: Validation, cleaning, and transformation

## 📝 Acknowledgments

Project completed as part of the Data Engineering Bootcamp by Navid Shirzadi, demonstrating practical skills in building production-ready data pipelines.

---

⭐ **Star this repo if you found it helpful!**
