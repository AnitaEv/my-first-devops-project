# My First DevOps Project 🚀

Это мой первый учебный проект по автоматизации развертывания (DevOps). Приложение на **Python (FastAPI)**, упакованное в **Docker** и запущенное в локальном кластере **Kubernetes (KinD)**.

## Основные компоненты:
- **App**: Python API на базе FastAPI.
- **Docker**: Контейнеризация приложения.
- **Kubernetes (k8s)**: Манифесты для развертывания Deployment и Service.
- **KinD**: Локальный Kubernetes кластер.

## Как запустить проект локально:

1. **Сборка Docker-образа:**
   ```bash
   cd app
   docker build -t my-devops-app:v1 .
   cd ..
   ```

2. **Загрузка образа в кластер KinD:**
   ```bash
   kind load docker-image my-devops-app:v1 --name my-app-cluster
   ```

3. **Развертывание в Kubernetes:**
   ```bash
   kubectl apply -f k8s/app.yaml
   ```

4. **Доступ к приложению:**
   ```bash
   kubectl port-forward svc/my-app-service 8080:80
   ```
   После этого приложение доступно по адресу: [http://localhost:8080](http://localhost:8080)

## Автор
**AnitaEv** — начинающий DevOps инженер.
