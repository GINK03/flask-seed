function register() {
    var form = document.forms.main;
    
    var username = form.username.value;
    var email = form.email.value;
    var password = form.password.value;
    
    // Initialize Firebase
    var config = {
      apiKey: "AIzaSyDMGRnn2gq3my_1c1aNjCo8JxJCA5S7zMg",
      authDomain: "wild-yukikaze.firebaseapp.com",
      databaseURL: "https://wild-yukikaze.firebaseio.com",
      projectId: "wild-yukikaze",
      storageBucket: "wild-yukikaze.appspot.com",
      messagingSenderId: "779205869653"
    };
    firebase.initializeApp(config);
    
    // Initialize Cloud Firestore through Firebase
    var db = firebase.firestore();
    
    // Register the user
    firebase.auth().createUserWithEmailAndPassword(email, password).catch(function(error) {
        // Handle Errors here.
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log(errorCode, errorMessage);
    });
    
    firebase.auth().onAuthStateChanged(function(user) {
        if (user) {
        // User is signed in.
            var displayName = user.displayName;
            var email = user.email;
            var emailVerified = user.emailVerified;
            var photoURL = user.photoURL;
            var isAnonymous = user.isAnonymous;
            var uid = user.uid;
            var providerData = user.providerData;
            
            console.log(uid);
            
            db.collection("users").doc(uid).set({
                username: username
            })
            .then(function() {
                console.log("Document successfully written!");
            })
            .catch(function(error) {
                console.error("Error adding document: ", error);
            });
            
        } else {
            // User is signed out.
            // ...
        }
    });
}
