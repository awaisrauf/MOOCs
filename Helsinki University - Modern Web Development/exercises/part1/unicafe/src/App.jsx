import {useState} from 'react'

// const ShowAvg = ({good, neutral, bad}) => {
//   const total = good + neutral + bad
//   const  avg = ((1*good) + (-1*bad))/total
//   return(
//     <> 
//     <p>avg {avg}</p>
//     </>
//   )
// }

// const ShowPosPercent = ({good, neutral, bad}) => {
//   const total = good + neutral + bad
//   const  posPercent = good/total
//   return(
//     <> 
//     <p> positive {posPercent}%</p>
//     </>
//   )
// }

const Statistics = (props) => {
  const {good, neutral, bad} = props
  const all = good+neutral+bad
  const weightedSum = (1*good) + (0*neutral) + (-1*bad)
  const avg = weightedSum/all
  const posPercent = good/all
  if (all !==0) {
  return (
    <div>
      <p>good {good} </p>
      <p>neutral {neutral}</p>
      <p>bad {bad}</p>
      <p>all {all}</p>
      <p>avg {avg}</p>
      <p>positive {posPercent}</p>
    </div>
  )
  }
return (
  <div>
    <p>No feedback has given</p>
  </div>
)
}

const App = () => {
  // saving clicks of button
  const [good, setGood] = useState(0)
  const [neutral, setNeutral] = useState(0)
  const [bad, setBad] = useState(0)

  const actionGood = () => setGood(good+1)
  const actionBad = () => setBad(bad+1)
  const actionNeutral = () => setNeutral(neutral+1)

  const allVals = [good, neutral, bad]

  return (
    <div>
      <h1> give feedback</h1>
      <button onClick={actionGood}>good</button>
      <button onClick={actionNeutral}>neutral</button>
      <button onClick={actionBad}>bad</button>

      <h1>statistics</h1>
      <Statistics good={good} neutral={neutral} bad={bad}/>
        
    </div>
  )
}
export default App