Option Explicit

Sub CompareWordTableAndExcelValue()
    Dim wordFilePath As String
    Dim excelFilePath As String
    Dim wordApp As Object ' Word.Application
    Dim wordDoc As Object ' Word.Document
    Dim lastTable As Object ' Word.Table
    Dim rowOffset As Integer
    Dim wordValue As String
    Dim excelValue As String
    Dim errorFlag As Boolean
    Dim excelRow As Integer
    
    ' 1. Wordファイルを指定
    wordFilePath = Application.GetOpenFilename("Word Files (*.doc;*.docx), *.doc;*.docx")
    If wordFilePath = "False" Then Exit Sub
    
    ' 2. Excelファイルを指定
    excelFilePath = Application.GetOpenFilename("Excel Files (*.xls;*.xlsx), *.xls;*.xlsx")
    If excelFilePath = "False" Then Exit Sub
    
    ' Wordアプリケーションを起動
    Set wordApp = CreateObject("Word.Application")
    wordApp.Visible = False ' Wordを表示しない
    
    ' Wordファイルを開く
    Set wordDoc = wordApp.Documents.Open(wordFilePath)
    
    ' 3. 最後の表を取得
    Set lastTable = wordDoc.Tables(wordDoc.Tables.Count)
    
    ' 4～6を繰り返し行う
    rowOffset = 0
    errorFlag = False
    excelRow = 2 ' G列のセル参照先行を初期化
    Do
        ' 4. テーブルの値を取得して連結
        wordValue = lastTable.Cell(2 + rowOffset, 2).Range.Text & vbCrLf & lastTable.Cell(2 + rowOffset, 4).Range.Text
        
        ' 5. Excelの値と比較
        On Error Resume Next ' エラーが発生しても処理を続行
        excelValue = Replace(ThisWorkbook.Sheets(1).Cells(excelRow, 7).Value, vbCrLf, "") ' 改行を削除して値を取得
        On Error GoTo 0 ' エラーハンドリングを元に戻す
        
        ' 6. 比較結果を表示
        If excelValue <> wordValue Then
            MsgBox "エラー：Wordファイルの値とExcelファイルの値が一致しません。", vbExclamation, "エラー"
            errorFlag = True
            Exit Do
        End If
        
        ' 次の行を指定
        rowOffset = rowOffset + 2
        excelRow = excelRow + 1 ' G列のセル参照先行を1行ずつ増やす
        
    Loop While lastTable.Cell(2 + rowOffset, 2).Range.Text <> "" And lastTable.Cell(2 + rowOffset, 4).Range.Text <> ""
    
    ' Word関連のオブジェクトを解放
    wordDoc.Close
    wordApp.Quit
    Set wordDoc = Nothing
    Set wordApp = Nothing
    
    ' エラーがない場合は完了メッセージを表示
    If Not errorFlag Then
        MsgBox "比較が完了しました。", vbInformation, "完了"
    End If
End Sub

