*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Register Page Should Open

*** Test Cases ***
Register With Valid Username And password
    Set Username     kalleeeee
    Set Password     kalle123
    Set Password Confirmation        kalle123
    Submit Credentials 
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username   ka
    Set Password   kalle123
    Set Password Confirmation        kalle123
    Submit Credentials
    Register Should Fail With Message    Virheellinen

Register With Valid Username And Too Short Password
    Set Username   kalleee
    Set Password   kalle
    Set Password Confirmation        kalle
    Submit Credentials
    Register Should Fail With Message    Virheellinen

Register With Nonmatching Password And Password Confirmation
    Set Username   kalleee
    Set Password   kalle1234
    Set Password Confirmation        kalle
    Submit Credentials
    Register Should Fail With Message    Passwords don't match



*** Keywords***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password   password   ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password   password_confirmation   ${password_confirmation}

Create User And Register Page Should Open
    Go To Register Page
    Register Page Should Be Open