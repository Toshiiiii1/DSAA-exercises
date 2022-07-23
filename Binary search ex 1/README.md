Source: https://codelearn.io/learning/cau-truc-du-lieu-va-giai-thuat/826905

Ý tưởng thuật toán:

1. Tạo mảng b với b[0] = a[0], b[i] = b[i-1] + a[i] . Mục đích cần làm là tìm vị trí l và i sao cho b[i] - b[l] = s

2. Dùng biến i duyệt mảng b đến khi b[i] > s , tìm giá trị b[i]-s trong mảng a, khi đó chỉ cần duyệt mảng a từ l+1 đến i là ra kết quả của bài toán