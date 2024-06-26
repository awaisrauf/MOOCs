import { useState } from 'react'

const getRandomNum = (maxVal) => {
  const randVal = Math.floor(Math.random()*maxVal)
  return randVal
}

const argMax = (array) => {
  if (array.length == 0){
    return -1
  }

  let maxVal = array[0]
  let maxIdx = 0
  for (let i = 1; i < array.length; i++){
    if( array[i] > maxVal){
      maxIdx = i
      maxVal = array[i]
    }
  }

return maxIdx

}

const App = () => {
  const anecdotes = [
    'If it hurts, do it more often.',
    'Adding manpower to a late software project makes it later!',
    'The first 90 percent of the code accounts for the first 90 percent of the development time...The remaining 10 percent of the code accounts for the other 90 percent of the development time.',
    'Any fool can write code that a computer can understand. Good programmers write code that humans can understand.',
    'Premature optimization is the root of all evil.',
    'Debugging is twice as hard as writing the code in the first place. Therefore, if you write the code as cleverly as possible, you are, by definition, not smart enough to debug it.',
    'Programming without an extremely heavy use of console.log is same as if a doctor would refuse to use x-rays or blood tests when diagnosing patients.',
    'The only way to go fast, is to go well.'
  ]

  const [selected, setSelected] = useState(0)
  const numAnecdotes = anecdotes.length
  // set votes
  const [votes, setVote] = useState(new Array(numAnecdotes).fill(0))
  
  // handle next button logic
  const NextButtonAction = () => {
    const randomNum = getRandomNum(numAnecdotes)
    setSelected(randomNum)
  }

  // updates votes
  const VoteButtonAction = () => {
    const VoteButtonHandler = () => {
      console.log(typeof votes[0], votes[0])
      const newArray = [...votes]
      console.log('before', typeof newArray[selected])
      newArray[selected] += 1
      console.log(typeof newArray[0], newArray[0])
      setVote(newArray)
    }
    return VoteButtonHandler
  }

  // find max vote anecodte
  const ShowMaxVoteAnecdote = () => {
    const maxVoteIdx = argMax(votes)
    return (
      <div>
        <p>{anecdotes[maxVoteIdx]}</p> 
        <p>has {votes[maxVoteIdx]} votes</p>
      </div>
    )
  } 

  return (
    <div>
      <h1>Anecdote of the day</h1>
      <p>{anecdotes[selected]} </p>
      <p> votes {votes[selected]}</p>
      <button onClick={VoteButtonAction(selected)}>vote</button>
      <button onClick={NextButtonAction}> next anecdote</button>
      <h1>Anecdote with most votes</h1>
      <ShowMaxVoteAnecdote />


    </div>
  )
}

export default App