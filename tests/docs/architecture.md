# M-PESA Shield - System Architecture

## 1. Architecture Overview

M-PESA Shield uses a simple client-server architecture.

The frontend communicates with a Python backend
through a REST API.

---

# 2. High-Level Architecture

```text
+----------------------+
|       User           |
+----------+-----------+
           |
           v
+----------------------+
| HTML / CSS / JS      |
|      Frontend        |
+----------+-----------+
           |
           | HTTP POST /analyze
           v
+----------------------+
|      FastAPI         |
|       Backend        |
+----------+-----------+
           |
           v
+----------------------+
|  Python Analyzer     |
|  Rule-Based Engine   |
+----------+-----------+
           |
           v
+----------------------+
| Risk Assessment      |
| Score + Category     |
+----------+-----------+
           |
           v
+----------------------+
|     JSON Response    |
+----------+-----------+
           |
           v
+----------------------+
|      Frontend        |
| Display Result       |
+----------------------+
           |
           v
+----------------------+
|       User           |
+----------------------+