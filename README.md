# SurveilNet – Trade Surveillance & Anomaly Detection Platform

**Tech Stack:** Apache Kafka · Apache Spark Streaming · HBase · Presto · Java · Protobuf · Kubernetes · Python

---

## 📌 Overview

**SurveilNet** is a real-time trade surveillance platform built to detect suspicious financial activities such as spoofing, layering, and wash trading. It processes high-volume trade events, applies business logic to detect anomalies, and scales horizontally using modern big data and cloud-native technologies.

---

## 🔍 Key Features

- ⚡ **Real-Time Data Processing:** Ingests millions of trade events per day using Apache Kafka and processes them via Spark Streaming.
- 📦 **Compact Serialization:** Uses Protobuf for efficient and cross-platform data serialization.
- 🧠 **Anomaly Detection:** Identifies irregular trading behaviors (e.g., large-volume spikes, spoofing) and flags them for investigation.
- ☸️ **Kubernetes Deployments:** Ready-to-run manifests for scalable deployment in cloud-native environments.
- 🔍 **Presto Integration:** Allows fast, ad-hoc querying on enriched datasets for surveillance analytics.

---

## 🧱 Project Structure

SurveilNet/
├── src/
│ ├── kafka_producer/ # Simulated Kafka trade event producer
│ └── spark_streaming/ # Spark job for real-time filtering and detection
├── configs/ # Config files and schemas
├── k8s/ # Kubernetes deployment manifests
├── scripts/ # Optional helper scripts
└── README.md # Project documentation

yaml
Copy
Edit

---

## 🛠 Setup Instructions

### 📥 1. Clone the Repository

```bash
git clone https://github.com/rahulrn9/SurveilNet.git
cd SurveilNet
⚙️ 2. Start Kafka and Zookeeper
You can use Docker Compose or a local installation.

bash
Copy
Edit
docker run -d --name zookeeper -p 2181:2181 zookeeper
docker run -d --name kafka -p 9092:9092 \
  -e KAFKA_ZOOKEEPER_CONNECT=zookeeper:2181 \
  -e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://localhost:9092 \
  -e KAFKA_LISTENERS=PLAINTEXT://0.0.0.0:9092 \
  --network host \
  confluentinc/cp-kafka
🧪 3. Run Kafka Producer
Sends synthetic trade events to the Kafka topic trade-events.

bash
Copy
Edit
cd src/kafka_producer
python producer.py
🔄 4. Run Spark Streaming Job
You can run locally or submit it to a Spark cluster:

bash
Copy
Edit
cd src/spark_streaming
spark-submit streaming_job.py
☸️ 5. Kubernetes Deployment
Deploy the Spark job in a Kubernetes cluster:

bash
Copy
Edit
kubectl apply -f k8s/deployment.yaml
Ensure the image and volume mounts are configured to match your cluster setup.

📦 Sample Trade Event Format
json
Copy
Edit
{
  "user_id": 1024,
  "symbol": "TSLA",
  "action": "BUY",
  "quantity": 800,
  "timestamp": 1720254012
}
📊 Future Enhancements
Integrate HBase or Snowflake for historical data storage

Alerting system with Slack/Email/Webhooks for flagged trades

Add Prometheus + Grafana for monitoring Spark job metrics

Support for Flink or Beam for enhanced stream processing flexibility

🤝 Contributing
Pull requests and forks are welcome! Please raise an issue to discuss your ideas before opening a major PR.

