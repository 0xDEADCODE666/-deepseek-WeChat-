' 显示提示信息
MsgBox "需要更改文件！！" & vbCrLf & _
       "打开""C:\deepseek-on-wechat\config.py""" & vbCrLf & _
       "选择使用记事本打开修改需要的信息即可运行", _
       vbInformation + vbOKOnly, _
       "配置文件修改提示"

' 创建Shell对象
Set WshShell = CreateObject("WScript.Shell")

' 尝试用记事本打开配置文件
On Error Resume Next ' 防止路径错误导致脚本崩溃
WshShell.Run "notepad.exe C:\deepseek-on-wechat\config.py", 1, True
If Err.Number <> 0 Then
    MsgBox "打开文件失败，请检查文件路径是否存在", vbCritical, "错误"
End If
On Error Goto 0

' 清理对象
Set WshShell = Nothing