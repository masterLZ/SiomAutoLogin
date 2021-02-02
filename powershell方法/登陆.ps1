$url="http://210.72.9.2/ac_portal/default/pc.html?template=default&tabs=pwd&vlanid=0&_ID_=0&switch_url=&url=http://210.72.9.2/homepage/index.html&controller_type=&mac=18-60-24-a7-ae-53"
$ie=new-object -com "InternetExplorer.Application"
$ie.Visible=$true
$ie.Navigate($url)
    $milliseconds=0
    $maxMilliseconds = 10000
    while($ie.Busy)
    {
      if($milliseconds -gt $maxMilliseconds)
      {
        throw 'Wait ie ready timeout.'
      }
      sleep -Milliseconds 100
      $milliseconds+=100
    }
Start-Sleep -m 3000
$ie.document.getelementbyid("password_name").value="lizhan" #用户名
Start-Sleep -m 500
$ie.document.getelementbyid("password_pwd").value="080416"  #密码
Start-Sleep -m 500
$ie.document.getelementbyid("password_submitBtn").click()
Start-Sleep -m 1000
$ie.quit()
Remove-Variable ie -Force