import time

def bubble_sort(data_list):
    n = len(data_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if data_list[j] > data_list[j+1]:
                data_list[j], data_list[j+1] = data_list[j+1], data_list[j]

if __name__ == "__main__":
    data_list = []

    with open("data.txt", "r", encoding="utf-8") as f:
        for line in f:
            # ":"로 분리 → 앞은 버리고 뒷부분만 사용
            if ":" in line:
                line = line.split(":", 1)[1]  # 첫 번째 ":" 뒤 내용만

            # 공백 제거 후 콤마로 분리
            numbers = line.strip().split(",")

            # 숫자만 리스트에 추가
            data_list.extend(int(num.strip()) for num in numbers if num.strip())
    
    # 결과 확인
    print("읽어온 데이터:", data_list)
    print(f"총 데이터 개수: {len(data_list)}")

    # Bubble Sort
    bubble_data_list = data_list
    start_time = time.time()
    bubble_sort(bubble_data_list)
    end_time = time.time()
    print(bubble_data_list)