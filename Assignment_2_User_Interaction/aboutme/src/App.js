import './App.css';
import mochi from './img/mochi.jpg';
import sky from './img/sky.jpg'

function App() {
  return (
    <div className="App">
      <h1>About Me</h1>
      <div class="center-align">
          <a href="https://github.com/ozwalf/Platform_Computing" target="_blank"><button class="buttonwidth">Github</button></a>
      </div>
      <br/>

      <div class="mainbody">
          <h2>General Info</h2>
          <div class="paragraph">
              <p>Hello! My name is Ricky Sirk and I am currently enrolled at CSUSB and am majoring in Computer Science. I don't really like talking about myself all the much so the information here will be concise.</p>
          </div>  

          <h2>Pets</h2>
          <div class="paragraph">
              <p>I have two dogs. One is called Sky and the other Mochi.</p>
              <img src={sky} title="Sky" alt="Sky" width="467rem"/>
              <img src={mochi} title="Mochi" alt="Mochi" width="300rem"/>
              
          </div>

          <h2>Hobbies</h2>
          <div class="paragraph">
              <p>I like to play videogames. The styling of this page was heavily inspired by NieR: Automata's UI design.</p>
              <p>If you wish to learn more about the UI, here is an official blog post from the UI designer of NieR.</p>
              <a href="https://www.platinumgames.com/official-blog/article/9624" target="_blank">  UI Design in NieR:Automata  </a>
          </div>  
          <br/>
      </div>
      <br/>
      <div class="center-align">
          <a href="https://github.com/ozwalf/Platform_Computing" target="_blank"><button class="buttonwidth">Github</button></a>
      </div>
      <br/>
    </div>
  );
}

export default App;
