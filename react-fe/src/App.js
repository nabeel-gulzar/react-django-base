import logo from './logo.svg';
import './App.css';
import axios from "axios";
import {useState} from "react";

function App() {
  const [message, setMessage] = useState([])


  const getPersons = () => {
    axios
        .get("http://localhost:8000/apis/django_app/persons/")
        .then((res) => setMessage(res.data))
        .catch((err) => console.log(err))
  }


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
          <ul>
            {message.map(person => <li key={person.identification_no}>{person.first_name}</li>)}
          </ul>
        <button onClick={getPersons}>
          Refresh Persons List
        </button>
      </header>
    </div>
  );
}

export default App;
