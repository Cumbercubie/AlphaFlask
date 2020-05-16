import openpyxl
def getQuestionsFromFile(filename,sheet):
  result_list = []
  try:
      dataWorkbook = openpyxl.load_workbook(filename=filename)
      sheet = dataWorkbook[sheet]
      for row in sheet:
        data = [x.value for x in row]
        result_list.append(data)
  except:
    raise Exception()
  return  result_list
# def main():
#   print(getQuestionsFromFile("static/questions.xlsx",'Sheet1'))
#
#
# if __name__ == '__main__':
#       main()
