from sys import stdin

def bitmap():
  test = int(stdin.readline())

  for t in range(int(test)):
      (row, col) = stdin.readline().split()
      rows = int(row)
      cols = int(col)
      bitmap = []
      for i in range(rows):
            line = stdin.readline().strip()
            bitmap.append(line)
      output = [[False for y in range(cols)] for x in range(rows)]
      pixel = []
      num_element = rows*cols
      vissited = 0
      for i in range(rows):
            for j in range(cols):
                if bitmap[i][j] == '1':
                    output[i][j] = 0
                    pixel.append((i,j))
                    vissited = vissited +1
      while vissited < num_element:
            temp_list = []
            for node in pixel:
                i = node[0]
                j = node[1]
                new_distance = output[i][j] + 1
                if i> 0 and output[i-1][j] is False :
                    output[i-1][j] = new_distance                    
                    temp_list.append((i-1,j))
                    vissited = vissited +1
                if i< rows-1 and output[i+1][j] is False:
                    output[i+1][j] =new_distance
                    temp_list.append((i+1,j))
                    vissited = vissited +1
                if j > 0 and output[i][j-1] is False:
                    output[i][j-1] =new_distance
                    temp_list.append((i,j-1))
                    vissited = vissited +1
                if j < cols-1 and output[i][j+1] is False :
                    output[i][j+1] =new_distance
                    temp_list.append((i,j+1))
                    vissited = vissited +1
            pixel = temp_list
            
      for line in output:
          s = map(str, line)
          print(" ".join(s))
      stdin.readline()    

if __name__ == '__main__':
    bitmap()