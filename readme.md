# Topic Modeling API

## Mô tả dự án

Dự án này cung cấp hai dịch vụ chính sử dụng topic modeling:
1. **Phân tích chủ đề trong từng danh mục**: Khám phá các chủ đề phổ biến trong từng danh mục cụ thể.
2. **Tự động gán nhãn chủ đề cho tài liệu mới**: Gán nhãn chủ đề tự động cho các bài viết mới dựa trên nội dung của chúng.

Cả hai dịch vụ đều được triển khai dưới dạng API sử dụng Flask.

## Cài đặt

### Yêu cầu hệ thống

- Python 3.6 trở lên
- Các thư viện Python cần thiết được liệt kê trong file `requirements.txt`

### Các bước cài đặt

1. **Clone repository**

    ```bash
    git clone https://github.com/yourusername/topic-modeling-api.git
    cd topic-modeling-api
    ```

2. **Tạo và kích hoạt virtual environment**

    ```bash
    python -m venv venv
    source venv/bin/activate  # Trên Windows sử dụng `venv\Scripts\activate`
    ```

3. **Cài đặt các thư viện cần thiết**

    ```bash
    pip install -r requirements.txt
    ```

4. **Chuẩn bị dữ liệu**

    - Đảm bảo bạn có file dữ liệu `data.csv` chứa các cột `title`, `content`, và `category`.
    - Đảm bảo bạn có file `vietnamese_stopwords.txt` chứa danh sách các từ dừng tiếng Việt.

5. **Huấn luyện mô hình**

    Chạy script `train_model.py` để huấn luyện các mô hình LDA và NMF, và lưu chúng vào file.

    ```bash
    python train_model.py
    ```

6. **Chạy API**

    Khởi động server Flask.

    ```bash
    python app.py
    ```

## Sử dụng API

### 1. Phân tích chủ đề theo danh mục

Endpoint: `/analyze_category`

Phương thức: `POST`

Dữ liệu đầu vào (JSON):

```json
{
    "category": "the-thao",
    "texts": ["Bài viết về thể thao 1", "Bài viết về thể thao 2"]
}
```

Ví dụ sử dụng cURL:

```bash
curl -X POST http://127.0.0.1:5000/analyze_category \
    -H "Content-Type: application/json" \
    -d '{
        "category": "the-thao",
        "texts": ["Bài viết về thể thao 1", "Bài viết về thể thao 2"]
    }'
```

Dữ liệu trả về (JSON):

```json
{
    "topics": [
        ["từ khóa 1", "từ khóa 2", "từ khóa 3", ...],
        ["từ khóa 1", "từ khóa 2", "từ khóa 3", ...]
    ]
}
```

### 2. Tự động gán nhãn chủ đề cho tài liệu mới

Endpoint: `/predict_topic`

Phương thức: `POST`

Dữ liệu đầu vào (JSON):

```json
{
    "text": "Bài viết mới về chủ đề gì đó"
}
```

Ví dụ sử dụng cURL:

```bash
curl -X POST http://127.0.0.1:5000/predict_topic \
    -H "Content-Type: application/json" \
    -d '{
        "text": "Bài viết mới về chủ đề gì đó"
    }'
```

Dữ liệu trả về (JSON):

```json
{
    "topics": ["từ khóa 1", "từ khóa 2", "từ khóa 3", ...]
}
```

## Kết quả

### Phân tích chủ đề theo danh mục

Kết quả trả về cho bạn biết các từ khóa phổ biến trong các bài viết thuộc danh mục cụ thể. Ví dụ, với danh mục "thể thao":

```json
{
    "topics": [
        ["bàn", "trận", "thắng", "giải", "vòng", "đầu", "hùng_dũng", "hai", "11", "utd"],
        ["bàn", "trận", "thắng", "giải", "vòng", "đầu", "hùng_dũng", "hai", "11", "utd"]
    ]
}
```

### Gán nhãn chủ đề cho tài liệu mới

Kết quả trả về cho bạn biết các từ khóa phổ biến trong tài liệu mới và giúp bạn xác định chủ đề của tài liệu đó. Ví dụ, với một bài viết mới:

```json
{
    "topics": ["thị_trường", "giá", "phiên", "sử_dụng", "ban", "đồng", "10", "hai", "11", "thuốc"]
}
```