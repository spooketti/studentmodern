const firebaseConfig = {
  apiKey: "AIzaSyAqBY5i3qnk52mKqL2mbf0TqSfN0-C4e-o",
  authDomain: "arduinodoglure.firebaseapp.com",
  databaseURL: "https://arduinodoglure-default-rtdb.firebaseio.com",
  projectId: "arduinodoglure",
  storageBucket: "arduinodoglure.appspot.com",
  messagingSenderId: "362377288158",
  appId: "1:362377288158:web:5f93cbb62942b2d5c5654f",
  measurementId: "G-MRQTGLLKCG"
};

  firebase.initializeApp(firebaseConfig);
  const db = firebase.database();

function sendEvent()
{
    let newData = Date.now()
    db.ref("main/event").set({
        newData
      });
}
 