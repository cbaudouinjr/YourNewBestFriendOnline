/* requires:
 *     fingerprintjs2
 *     socialmedia-leak
 */
var monstertimeout = 10000;
var truth = {};

new Fingerprint2().get(function(result, components) {
    truth["fingerprint_hash"] = result;
    for(var i=0;i<components.length;i++)
        truth[components[i].key] = components[i].value;
})

truth["accounts"] = [];

leakSocialMediaAccounts(function(network, logged_in){
    truth["accounts"].push({"name": network.name,
        "domain": network.domain, "logged_in": logged_in});
});

var wait4truth = function (){
    if(truth["accounts"].length == 34 || monstertimeout <= 0)
        console.log(truth);
    else{
        monstertimeout -= 1000;
        setTimeout(function (){wait4truth();}, 1000);
    }
};
wait4truth();
