import { defineStore } from 'pinia'

export const useCollectionPointStore = defineStore('collectionpoint', () => {
  const allDisctrict = ref([
        { location: 'Ampara', value: 'ampara' },
        { location: 'Anuradhapura', value: 'anuradhapura' },
        { location: 'Badulla', value: 'badulla' },
        { location: 'Batticaloa', value: 'batticaloa' },
        { location: 'Colombo', value: 'colombo' },
        { location: 'Galle', value: 'galle' },
        { location: 'Gampaha', value: 'gampaha' },
        { location: 'Hambantota', value: 'hambantota' },
        { location: 'Jaffna', value: 'jaffna' },
        { location: 'Kalutara', value: 'kalutara' },
        { location: 'Kandy', value: 'kandy' },
        { location: 'Kegalle', value: 'kegalle' },
        { location: 'Kilinochchi', value: 'kilinochchi' },
        { location: 'Kurunegala', value: 'kurunegala' },
        { location: 'Mannar', value: 'mannar' },
        { location: 'Matale', value: 'matale' },
        { location: 'Matara', value: 'matara' },
        { location: 'Monaragala', value: 'monaragala' },
        { location: 'Mullaitivu', value: 'mullaitivu' },
        { location: 'Nuwara Eliya', value: 'nuwara-eliya' },
        { location: 'Polonnaruwa', value: 'polonnaruwa' },
        { location: 'Puttalam', value: 'puttalam' },
        { location: 'Ratnapura', value: 'ratnapura' },
        { location: 'Trincomalee', value: 'trincomalee' },
        { location: 'Vavuniya', value: 'vavuniya' }
    ])

    const organizationTypes = [
        'individual',
        'non profit organization',
        'community',
        'temple',
        'mosque',
    ]

    const collectItems = ref([])
    const district = ref(null)
    const town = ref(null)
    const geoLocation = ref(null)
    const nearestPlace = ref(null)
    const distributedTo = ref(null)
    // const deliveryMethod = ref(null)
    const endDate = ref(null)
    const organization = ref(null)
    const firstName = ref(null)
    const mobileNumber = ref(null)
    const description = ref(null)
    const getLocaitonDetails = ref(null)
    const allLocationList = ref([])
    const loadedDistrict = ref(null)

  return { allDisctrict, collectItems, district, town, nearestPlace, distributedTo, endDate, geoLocation, organizationTypes, organization, firstName, mobileNumber, description, getLocaitonDetails, allLocationList, loadedDistrict }
})