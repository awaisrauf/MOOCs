import {useState} from 'react'

// const calcAvg = ({good, neutral, bad}) => {
//   avg = (good_neutral+bad)
//   return(
//     <>avg</>
//   )
// }



const App = () => {
  // saving clicks of button
  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  const actionGood = () => setGood(good+1)
  const actionBad = () => setBad(bad+1)
  const actionNeutral = () => setNeutral(neutral+1)

  return (
    <div>
      <h1> give feedback</h1>
      <button onClick={actionGood}>good</button>
      <button onClick={actionNeutral}>neutral</button>
      <button onClick={actionBad}>bad</button>

      <h1>statistics</h1>
      <p>good {good} </p>
      <p>neutral {neutral}</p>
      <p>bad {bad}</p>
      {/* <p>all {}</p> */}
      {/* <p>average {calcAvg()}</p> */}
      {/* <p>positive {}</p> */}
        
    </div>
  )
}
export default App