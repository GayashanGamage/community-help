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

  return { allDisctrict  }
})