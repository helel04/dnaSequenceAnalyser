division_a = [
    {"uid": 101, "name": "Aarav Sharma", "marks": 85, "division": "A"},
    {"uid": 103, "name": "Ananya Patel", "marks": 92, "division": "A"},
    {"uid": 105, "name": "Arjun Desai", "marks": 78, "division": "A"},
    {"uid": 107, "name": "Diya Singh", "marks": 88, "division": "A"},
    {"uid": 109, "name": "Ishaan Kumar", "marks": 95, "division": "A"},
    {"uid": 111, "name": "Kavya Mehta", "marks": 82, "division": "A"},
    {"uid": 113, "name": "Krishna Reddy", "marks": 91, "division": "A"},
    {"uid": 115, "name": "Meera Joshi", "marks": 76, "division": "A"},
    {"uid": 117, "name": "Nisha Gupta", "marks": 89, "division": "A"},
    {"uid": 119, "name": "Pranav Shah", "marks": 84, "division": "A"},
    {"uid": 121, "name": "Riya Verma", "marks": 93, "division": "A"},
    {"uid": 123, "name": "Rohan Nair", "marks": 80, "division": "A"},
    {"uid": 125, "name": "Sanya Pillai", "marks": 87, "division": "A"},
    {"uid": 127, "name": "Tanvi Rao", "marks": 94, "division": "A"},
    {"uid": 129, "name": "Vivek Iyer", "marks": 81, "division": "A"}
]
division_b = [
    {"uid": 102, "name": "Aditi Kapoor", "marks": 86, "division": "B"},
    {"uid": 104, "name": "Aditya Malhotra", "marks": 79, "division": "B"},
    {"uid": 106, "name": "Arnav Thakur", "marks": 90, "division": "B"},
    {"uid": 108, "name": "Divya Agarwal", "marks": 83, "division": "B"},
    {"uid": 110, "name": "Harsh Pandey", "marks": 96, "division": "B"},
    {"uid": 112, "name": "Isha Bansal", "marks": 77, "division": "B"},
    {"uid": 114, "name": "Karan Saxena", "marks": 88, "division": "B"},
    {"uid": 116, "name": "Lakshmi Menon", "marks": 92, "division": "B"},
    {"uid": 118, "name": "Mohit Chopra", "marks": 85, "division": "B"},
    {"uid": 120, "name": "Neha Bhatia", "marks": 81, "division": "B"},
    {"uid": 122, "name": "Pooja Sinha", "marks": 94, "division": "B"},
    {"uid": 124, "name": "Rahul Mishra", "marks": 89, "division": "B"},
    {"uid": 126, "name": "Shreya Tiwari", "marks": 87, "division": "B"},
    {"uid": 128, "name": "Varun Dubey", "marks": 91, "division": "B"},
    {"uid": 130, "name": "Yash Kulkarni", "marks": 84, "division": "B"}
]
def standard_merge(div_a, div_b):
    result = []
    i, j = 0, 0
    m, n = len(div_a), len(div_b)
    while i < m and j < n:
        if div_a[i]['uid'] <= div_b[j]['uid']:
            result.append(div_a[i])
            i += 1
        else:
            result.append(div_b[j])
            j += 1
    result.extend(div_a[i:])
    result.extend(div_b[j:])
    return result
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and (arr[left]['marks'] > arr[largest]['marks'] or (arr[left]['marks'] == arr[largest]['marks'] and arr[left]['uid'] < arr[largest]['uid'])):
        largest = left
    if right < n and (arr[right]['marks'] > arr[largest]['marks'] or (arr[right]['marks'] == arr[largest]['marks'] and arr[right]['uid'] < arr[largest]['uid'])):
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
def reorder_by_marks(student_list):
    n = len(student_list)
    for i in range(n // 2 - 1, -1, -1):
        heapify(student_list, n, i)
    for i in range(n - 1, 0, -1):
        student_list[0], student_list[i] = student_list[i], student_list[0]
        heapify(student_list, i, 0)
    return student_list
def search_by_uid(student_list, target_uid):
    left, right = 0, len(student_list) - 1
    comparisons = 0
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if student_list[mid]['uid'] == target_uid:
            return student_list[mid], comparisons
        elif student_list[mid]['uid'] < target_uid:
            left = mid + 1
        else:
            right = mid - 1
    return None, comparisons
if __name__ == "__main__":
    print("=" * 70)
    print("UNIVERSITY RESULT PROCESSING SYSTEM - MCA DIVISIONS")
    print("MERGE: STANDARD MERGE ALGORITHM (STABLE, O(n+m))")
    print("=" * 70)
    print("\n[OPERATION 1] MERGING DIVISION A & B - STANDARD MERGE")
    print("-" * 70)
    merged_students = standard_merge(division_a.copy(), division_b.copy())
    print(f"Successfully merged {len(merged_students)} students (sorted by UID)")
    print("First 5 students:")
    for i in range(5):
        s = merged_students[i]
        print(f"  {i+1}. UID: {s['uid']}, Name: {s['name']}, Marks: {s['marks']}, Div: {s['division']}")
    print("\nLast 3 students:")
    for i in range(len(merged_students)-3, len(merged_students)):
        s = merged_students[i]
        print(f"  {i+1}. UID: {s['uid']}, Name: {s['name']}, Marks: {s['marks']}, Div: {s['division']}")
    print("\n" + "=" * 70)
    print("[OPERATION 2] GENERATING MERIT LIST (Sorted by Marks)")
    print("-" * 70)
    merit_list = merged_students.copy()
    reorder_by_marks(merit_list)
    print("Top 10 Students:")
    for i in range(10):
        s = merit_list[-(i+1)]
        print(f"  Rank {i+1:2d}: {s['name']:20s} | UID: {s['uid']} | Marks: {s['marks']} | Div {s['division']}")
    print("\n" + "=" * 70)
    print("[OPERATION 3] SEARCHING STUDENTS BY UID")
    print("-" * 70)
    search_targets = [115, 122, 101, 130, 999]
    for uid in search_targets:
        result, comps = search_by_uid(merged_students, uid)
        if result:
            print(f"\nUID {uid}: FOUND (Comparisons: {comps})")
            print(f"  → Name: {result['name']}, Marks: {result['marks']}, Division: {result['division']}")
        else:
            print(f"\nUID {uid}: NOT FOUND (Comparisons: {comps})")
    print("\n" + "=" * 70)
    print("ALGORITHM SUMMARY")
    print("=" * 70)
    print("1. Merge: STANDARD MERGE - O(n+m) time, O(n+m) space, STABLE")
    print("2. Reorder: Heap Sort - O(n log n) time, O(1) space")
    print("3. Search: Binary Search - O(log n) time, O(1) space")
    print("Data Structure: Dynamic Array (Python List)")
    print("=" * 70)
