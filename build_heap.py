# python3


def build_heap(data):
    swaps = []
    
    last_parent_index = len(data) // 2 - 1
    for i in range(last_parent_index, -1, -1):
        heapify(data, i, swaps)
        
    return swaps


def heapify(data, index, swaps):
    smaller_index = index
    
    left_child_index = 2 * index + 1
    if (left_child_index < len(data) and data[left_child_index] < data[smaller_index]):
        smaller_index = left_child_index
    
    right_child_index = 2 * index + 2
    if (right_child_index < len(data) and data[right_child_index] < data[smaller_index]):
        smaller_index = right_child_index
        
    if (smaller_index == index):
        return
    
    swaps.append([index,smaller_index])
    
    temp = data[index]
    data[index] = data[smaller_index]
    data[smaller_index] = temp
    
    heapify(data, smaller_index, swaps)
    
    
def main():
    command = input()
    if "F" in command:
        file_name = input()
        path = "test/" + file_name
        if not "a" in file_name:
            contents = open(path, "r")
            text = contents.read()
            contents.close()
            partitioned = text.partition("\n")
            n = int(partitioned[0])
            data = partitioned[2].split(" ")
            assert len(data) == n
            
            swaps = build_heap(data)
            
            if (len(swaps) >= 4*len(data)):
                return
      
            print(len(swaps))
            for i, j in swaps:
                print(i, j)
            
        
    elif "I" in command:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
        
        swaps = build_heap(data)
        
        if (len(swaps) >= 4*len(data)):
            return
        
        print(len(swaps))
        for i, j in swaps:
            print(i, j)


if __name__ == "__main__":
    main()
