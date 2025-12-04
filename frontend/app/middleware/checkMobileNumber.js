import { useCollectionPointStore } from "@/store/collectionpoint"
import { navigateTo } from "#app"

export default defineNuxtRouteMiddleware((to, from) => {
    
    if(to.fullPath == '/collection/add/otp'){
        if(process.client){
            
            const collectionstore = useCollectionPointStore()
            const mnumber = localStorage.getItem('mobileNumber')
            
            if(mnumber !== null){
                collectionstore.mobileNumber = mnumber
                return
            }else{
                return navigateTo('/collection/add')
            }
        }else if(process.server){
            return navigateTo('/collection/add')
        }
    }
})


