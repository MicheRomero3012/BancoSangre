import{useEffect,useState} from 'react'
import { getAllTasks } from '../api/tasks.api'
import { TaskCard } from './TaskCard';
export function TasksList() {
    const [tasks, setTasks] = useState([]);      //paras que se ejecute cada que se entra a la pagina
useEffect(()=>{
    async function loadTasks(){
        const res= await getAllTasks();
        setTasks(res.data); 
    };
    loadTasks();
},[]);  
    return <div>
        {tasks.map(task=>(
                <TaskCard key={task.id} task={task} />
            ))}
    
    </div>;
}