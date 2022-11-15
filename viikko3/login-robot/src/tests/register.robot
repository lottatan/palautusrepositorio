*** Settings ***
Resource   resource.robot
Test Setup   Create User and Input Create Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   kallee   kalle123
    Output Should Contain    New user registered

Register With Already Taken Username And Valid Password
    Input Credentials   kalle   kalle123
    Output Should Contain    User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials   ka   kalle123
    Output Should Contain    Virheellinen

Register With Valid Username And Too Short Password
    Input Credentials   kalleee   kalle
    Output Should Contain    Virheellinen

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials   kalleeee   kallemoi
    Output Should Contain    Virheellinen


*** Keywords ***
Create User and Input Create Command
    Create User  kalle  kalle123
    Input Create Command