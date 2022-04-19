from PIL import Image, ImageDraw

class Reader:
  def __init__(self, content, width):
    self.TempWidth = int(width)
    self.render(content)
    
  def render(self, content):
    data = content.split("\n")
    header = data[0].split(" ")
    if header[0] == "VES":
      self.width = round(float(header[2]))
      self.height = round(float((header[3])))
      if self.TempWidth == "":
        self.output_width = self.width
        self.output_height = self.height
      else:
        self.output_width = round(float(self.TempWidth))
        self.output_height = int(self.height/self.width * self.output_width)
    self.img = Image.new('RGB', (self.output_width, self.output_height), (255,255,255))
    for line in data[1:]:
      splitL = line.split(" ")
      self.detect(splitL)
    
  def detect(self, line):
    if line == "\n":
      pass
    else:
      command = line[0]
      if command == "CLEAR":
        self.clear_im(self.hexColor(line[1]))
      elif command == "LINE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        thickness = self.convert_x(float(line[5]))
        color = self.hexColor(line[6])
        self.thick_line(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), thickness, color)
      elif command == "RECT":
        Ax = float(line[1])
        Ay = float(line[2])
        width = float(line[3])
        height = float(line[4])
        thickness = self.convert_x(float(line[5]))
        color = self.hexColor(line[6])
        self.rect(self.convert_point((Ax, Ay)), self.convert_x(width), self.convert_x(height), thickness, color)
      elif command == "TRIANGLE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        Cx = float(line[5])
        Cy = float(line[6])
        thickness = self.convert_x(float(line[7]))
        color = self.hexColor(line[8])
        self.triangle(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), self.convert_point((Cx, Cy)), thickness, color)
      elif command == "CIRCLE":
        Sx = float(line[1])
        Sy = float(line[2])
        r = self.convert_x(float(line[3]))
        thickness = self.convert_x(float(line[4]))
        color = self.hexColor(line[5])
        self.circle(self.convert_point((Sx, Sy)), r, thickness, color)
      elif  command == "FILL_CIRCLE":
        Sx = float(line[1])
        Sy = float(line[2])
        r = self.convert_x(float(line[3]))
        color = self.hexColor(line[4])
        self.filled_circle(self.convert_point((Sx, Sy)), r, color)
      elif command == "FILL_TRIANGLE":
        Ax = float(line[1])
        Ay = float(line[2])
        Bx = float(line[3])
        By = float(line[4])
        Cx = float(line[5])
        Cy = float(line[6])
        color = self.hexColor(line[7])
        self.filled_triangle(self.convert_point((Ax, Ay)), self.convert_point((Bx, By)), self.convert_point((Cx, Cy)), color)
      elif command == "FILL_RECT":
        Ax = float(line[1])
        Ay = float(line[2])
        width = float(line[3])
        height = float(line[4])
        color = self.hexColor(line[5])
        self.filled_rect(self.convert_point((Ax, Ay)), self.convert_x(width), self.convert_x(height), color)
        


  

  def clear_im(self, color):
    for i in range(self.output_width):
      for j in range(self.output_height):
        self.img.putpixel((i, j), color)
  
  def hexColor(self, color):
    self.color = color.replace("\n", "")
    r = self.hex2dec(self.color[1:3])
    g = self.hex2dec(self.color[3:5])
    b = self.hex2dec(self.color[5:])
  
    return (r, g, b)
  
  def hex2dec(self, hex_num):
    hex_num = hex_num.replace("\r", "")
    decimal = 0
    for index in range(len(hex_num)):
      num = hex_num[(index+1)*(-1)].upper()
      if ord("A") <= ord(num) <= ord("F"):
        num = ord(num) - 65 + 10
      else:
        num = int(num)
    
      decimal += num * 16 ** index
    return(decimal)

  def convert_x(self, x):
    return int(x/self.width * self.output_width)

  def convert_y(self, y):
    return int(y/self.height * self.output_height)

  def convert_point(self, X):
    return (self.convert_x(X[0]), self.convert_y(X[1]))
  
  def thick_line(self, A, B, thickness, color):
    pixels = self.linePixels(A, B)
    for X in pixels:
      self.filled_circle(X, thickness/2, color)
  
  def linePixels(self, A, B):
    pixels = []
    if A[0] == B[0]:
      if A[1] > B[1]:
        A,B = B,A
      for y in range(A[1], B[1] + 1):
        pixels.append((A[0], y))
    elif A[1] == B[1]:
      if A[0] > B[0]:
        A,B=B,A
      for x in range(A[0], B[0] + 1):
        pixels.append((x, A[1]))
    else:
      if A[0] > B[0]:
        A,B=B,A 
      dx = B[0] - A[0] 
      dy = B[1] - A[1]
      if (dy/dx) > 1:
        for y in range(min(A[1], B[1]), max(A[1],B[1]) + 1):
          x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
          pixels.append((x, y))
      else:
        for x in range(min(A[0], B[0]), max(A[0], B[0])+ 1):
          y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
          pixels.append((x,y))
    return pixels

  def filled_circle(self, S, r, color):
    for x in range(0, int(r/2**(1/2)) + 1):
      y = int((r**2 - x**2)**(1/2))

      self.line((x + S[0], y + S[1]), (x + S[0], -y + S[1]), color)
      self.line((y + S[0], x + S[1]), (y + S[0], -x + S[1]), color)
      self.line((-x + S[0], -y + S[1]), (-x + S[0], y + S[1]), color)
      self.line((-y + S[0], -x + S[1]), (-y + S[0], x + S[1]), color)
  
  def line(self, A, B, color):
    body = []
    if A[0] == B[0]:
      if A[1] > B[1]:
        A,B = B,A
      for y in range(A[1], B[1] + 1):
        body.append((A[0], y))
    elif A[1] == B[1]:
      if A[0] > B[0]:
        A,B=B,A
      for x in range(A[0], B[0] + 1):
        body.append((x, A[1]))
    else:
      if A[0] > B[0]:
        A,B=B,A 
      dx = B[0] - A[0] 
      dy = B[1] - A[1]
      if abs(dy/dx) > 1:
        for y in range(min(A[1], B[1]), max(A[1],B[1]) + 1):
          x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
          body.append((x,y))
      else:
        for x in range(min(A[0], B[0]), max(A[0], B[0])+ 1):
          y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
          body.append((x,y))
    self.overenie(body, color)
  
  def overenie(self, body, color):
    for bod in body:
      if bod[0] < 0 or bod[1] < 0 or bod[0] >= self.output_width or bod[1] >= self.output_height:
        pass
      else:
        self.img.putpixel(bod, color)
  
  def rect(self, A, width, height, thickness, color):
    self.thick_line(A, (A[0] + width, A[1]), thickness, color)
    self.thick_line((A[0] + width, A[1]), (A[0] + width, A[1] + height), thickness, color)
    self.thick_line((A[0] + width, A[1] + height), (A[0], A[1] + height), thickness, color)
    self.thick_line((A[0], A[1] + height), A, thickness, color)
  
  def triangle(self, A, B, C, thickness, color):

    self.thick_line(A, B, thickness, color)
    self.thick_line(B, C, thickness, color)
    self.thick_line(A, C, thickness, color)

  def circle(self, S, r, thickness, color):
    for x in range(0, int(r/2**(1/2)) + 1):
      y = int((r**2 - x**2)**(1/2))

      self.filled_circle((x + S[0], y + S[1]), thickness/2, color)
      self.filled_circle((y + S[0], x + S[1]), thickness/2, color)
      self.filled_circle((y + S[0], -x + S[1]), thickness/2, color)
      self.filled_circle((x + S[0], -y + S[1]), thickness/2, color)
      self.filled_circle((-x + S[0], -y + S[1]), thickness/2, color)
      self.filled_circle((-y + S[0], -x + S[1]), thickness/2, color)
      self.filled_circle((-y + S[0], x + S[1]), thickness/2, color)
      self.filled_circle((-x + S[0], y + S[1]), thickness/2, color)
  
  def filled_triangle(self, A, B, C, color):
    draw = ImageDraw.Draw(self.img)
    draw.polygon([(A), (B), (C)], fill = color)

  def filled_rect(self, A, width, height, color):
    body = []
    for x in range(A[0], A[0]+width):
      for y in range(A[1], A[1]+height):
        body.append((x,y))
    self.overenie(body, color)
  