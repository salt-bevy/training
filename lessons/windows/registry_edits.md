#### Editing the Windows Registry

One of the most danger-prone tasks of Windows administration happens when
a systems administrator must manually edit the Windows Registry. 
The "regedit" editor is clumsy, and the syntax of the entries is difficult.
Errors can lead to systems failure.

Salt comes to our rescue with the "reg" state commands.

Look in [salt.states.reg](https://docs.saltstack.com/en/latest/ref/states/all/salt.states.reg.html#module-salt.states.reg)
for full documentation. 
Simply stated: `reg.absent` removes a registry value,
`reg.key_absent` remove a registry key (with any sub-keys and values),
and `reg.present` creates or alters a key or value.

A practical working example is found in salt-bevy.  Windows 10 has a set of
applications of which Microsoft is very proud -- for example, the Edge browser.
If another application changes the file association for a given extension,
for example `.pdf`, and does not do it precisely according to a new formula
invented for Windows 10, then the OS will send the user a notification and
reset the association back to Edge.  
This can be prevented by re-writing the other application to obey the new rules,
or by setting registry entries to tell the OS to leave the values alone.

To apply the work-around, run 

`salt <windows-minion-id> state.apply windows.keep_my_file_associations`.

The example source code can be found in [bevy_srv/salt/windows/keep_my_file_assocations](../../../salt-bevy/bevy_srv/salt/windows/keep_my_file_associations.sls).
