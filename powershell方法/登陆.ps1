$url="http://1.1.1.2/ac_portal/default/pc.html?tabs=pwd"
$ie=new-object -com "InternetExplorer.Application"
$ie.Visible=$true
$ie.Navigate($url)
    $milliseconds=0
    $maxMilliseconds = 5000
    while($ie.Busy)
    {
      if($milliseconds -gt $maxMilliseconds)
      {
        throw 'Wait ie ready timeout.'
      }
      sleep -Milliseconds 100
      $milliseconds+=100
    }
$ie.document.getelementbyid("password_name").value="lizhan" #用户名
Start-Sleep -m 500
$ie.document.getelementbyid("password_pwd").value="080416"  #密码
Start-Sleep -m 500
$ie.document.getelementbyid("password_submitBtn").click()
Start-Sleep -m 1000
$ie.quit()
Remove-Variable ie -Force