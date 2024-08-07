import {useState} from 'react'

const Statistics = (props) => {
  const {good, neutral, bad } = props
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

const Button = (props) => {
  const {buttonAction, text} = props
  return (
  <button onClick={buttonAction}>{text}</button>
  )
}

const StatisticsLine = ({text, values}) => {
  const [good, neutral, bad] = values
  const all = good+neutral+bad
  const weightedSum = (1*good) + (0*neutral) + (-1*bad)
  const avg = (weightedSum/all).toFixed(2)
  const posPercent = (good/all).toFixed(2)

  const GetStats = ({label, val}) => {
    if (label!="positive"){
      return (
      <>
        <td>{label}</td> <td>{val}</td>
      </>
      )
      }
      return (
      <>
        <td>{label}</td> <td>{val}%</td>
      </>
      )

  }
  switch(text){
    case "good":
      return <GetStats label={text} val={good}/>
    case "bad":
      return <GetStats label={text} val={bad}/>
    case "neutral":
      return <GetStats label={text} val={good}/>
    case "all":
      return <GetStats label={text} val={good}/>
    case "average":
      return <GetStats label={text} val={avg}/>
    case "positive":
      return <GetStats label={text} val={posPercent}/>

    default:
        return 

  }
  
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
      <h1>give feedback</h1>
      <Button buttonAction={actionGood} text={'good'}/>
      <Button buttonAction={actionNeutral} text={'neutral'}/>
      <Button buttonAction={actionBad} text={'bad'}/>

      <h1>statistics</h1>
      <table>
          <tr> <StatisticsLine text={'good'} values={allVals}/> </tr>
          <tr> <StatisticsLine text={'neutral'} values={allVals}/> </tr>
          <tr> <StatisticsLine text={'bad'} values={allVals}/> </tr>
          <tr> <StatisticsLine text={'all'} values={allVals}/> </tr>
          <tr> <StatisticsLine text={'average'} values={allVals}/> </tr>
          <tr> <StatisticsLine text={'positive'} values={allVals}/> </tr>
      </table>
        
    </div>
  )
}
export default App


