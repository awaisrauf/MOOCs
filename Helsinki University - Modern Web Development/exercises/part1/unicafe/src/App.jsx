import {useState} from 'react'

const ShowAvg = ({good, neutral, bad}) => {
  const total = good + neutral + bad
  const  avg = ((1*good) + (-1*bad))/total
  return(
    <> 
    <p>avg {avg}</p>
    </>
  )
}

const ShowPosPercent = ({good, neutral, bad}) => {
  const total = good + neutral + bad
  const  posPercent = good/total
  return(
    <> 
    <p> positive {posPercent}%</p>
    </>
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
      <p>good {good} </p>
      <p>neutral {neutral}</p>
      <p>bad {bad}</p>
      <p>all {good+bad+neutral}</p>
      <ShowAvg good={good} neutral={neutral} bad={bad}/>
      <ShowPosPercent good={good} neutral={neutral} bad={bad}/>
        
    </div>
  )
}
export default App