# SurveilNet – Trade Surveillance & Anomaly Detection Platform

## Components
- Kafka Producer: Sends mock trade events.
- Spark Streaming Job: Consumes trade events and filters suspicious ones.
- Kubernetes Deployment: For Spark job execution in cluster.

## Usage
1. Start Kafka and Zookeeper.
2. Run `producer.py` to simulate trades.
3. Submit `streaming_job.py` to Spark or deploy on Kubernetes using `deployment.yaml`.
