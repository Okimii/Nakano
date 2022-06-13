from typing import ClassVar

__all__ = ["GatewayEvents"]


class GatewayEvents:
    Hello: ClassVar[str] = "Hello"
    Ready: ClassVar[str] = "Ready"
    Resumed: ClassVar[str] = "Resumed"
    Reconnect: ClassVar[str] = "Reconnect"
    Invalid_Session: ClassVar[str] = "Invalid_Session"
    Application_Command_Permissions_Update: ClassVar[
        str
    ] = "Application_Command_Permissions_Update"
    Channel_Create: ClassVar[str] = "Channel_Create"
    Channel_Update: ClassVar[str] = "Channel_Update"
    Channel_Delete: ClassVar[str] = "Channel_Delete"
    Channel_Pins_Update: ClassVar[str] = "Channel_Pins_Update"
    Thread_Create: ClassVar[str] = "Thread_Create"
    Thread_Update: ClassVar[str] = "Thread_Update"
    Thread_Delete: ClassVar[str] = "Thread_Delete"
    Thread_List_Sync: ClassVar[str] = "Thread_List_Sync"
    Thread_Member_Update: ClassVar[str] = "Thread_Member_Update"
    Thread_Members_Update: ClassVar[str] = "Thread_Members_Update"
    Guild_Create: ClassVar[str] = "Guild_Create"
    Guild_Update: ClassVar[str] = "Guild_Update"
    Guild_Delete: ClassVar[str] = "Guild_Delete"
    Guild_Ban_Add: ClassVar[str] = "Guild_Ban_Add"
    Guild_Ban_Remove: ClassVar[str] = "Guild_Ban_Remove"
    Guild_Emojis_Update: ClassVar[str] = "Guild_Emojis_Update"
    Guild_Stickers_Update: ClassVar[str] = "Guild_Stickers_Update"
    Guild_Integrations_Update: ClassVar[str] = "Guild_Integrations_Update"
    Guild_Member_Add: ClassVar[str] = "Guild_Member_Add"
    Guild_Member_Remove: ClassVar[str] = "Guild_Member_Remove"
    Guild_Member_Update: ClassVar[str] = "Guild_Member_Update"
    Guild_Members_Chunk: ClassVar[str] = "Guild_Members_Chunk"
    Guild_Role_Create: ClassVar[str] = "Guild_Role_Create"
    Guild_Role_Update: ClassVar[str] = "Guild_Role_Update"
    Guild_Role_Delete: ClassVar[str] = "Guild_Role_Delete"
    Guild_Scheduled_Event_Create: ClassVar[str] = "Guild_Scheduled_Event_Create"
    Guild_Scheduled_Event_Update: ClassVar[str] = "Guild_Scheduled_Event_Update"
    Guild_Scheduled_Event_Delete: ClassVar[str] = "Guild_Scheduled_Event_Delete"
    Guild_Scheduled_Event_User_Add: ClassVar[str] = "Guild_Scheduled_Event_User_Add"
    Guild_Scheduled_Event_User_Remove: ClassVar[
        str
    ] = "Guild_Scheduled_Event_User_Remove"
    Integration_Create: ClassVar[str] = "Integration_Create"
    Integration_Update: ClassVar[str] = "Integration_Update"
    Integration_Delete: ClassVar[str] = "Integration_Delete"
    Interaction_Create: ClassVar[str] = "Interaction_Create"
    Invite_Create: ClassVar[str] = "Invite_Create"
    Invite_Delete: ClassVar[str] = "Invite_Delete"
    Message_Create: ClassVar[str] = "Message_Create"
    Message_Update: ClassVar[str] = "Message_Update"
    Message_Delete: ClassVar[str] = "Message_Delete"
    Message_Delete_Bulk: ClassVar[str] = "Message_Delete_Bulk"
    Message_Reaction_Add: ClassVar[str] = "Message_Reaction_Add"
    Message_Reaction_Remove: ClassVar[str] = "Message_Reaction_Remove"
    Message_Reaction_Remove_All: ClassVar[str] = "Message_Reaction_Remove_All"
    Message_Reaction_Remove_Emoji: ClassVar[str] = "Message_Reaction_Remove_Emoji"
    Presence_Update: ClassVar[str] = "Presence_Update"
    Stage_Instance_Create: ClassVar[str] = "Stage_Instance_Create"
    Stage_Instance_Delete: ClassVar[str] = "Stage_Instance_Delete"
    Stage_Instance_Update: ClassVar[str] = "Stage_Instance_Update"
    Typing_Start: ClassVar[str] = "Typing_Start"
    User_Update: ClassVar[str] = "User_Update"
    Voice_State_Update: ClassVar[str] = "Voice_State_Update"
    Voice_Server_Update: ClassVar[str] = "Voice_Server_Update"
    Webhooks_Update: ClassVar[str] = "Webhooks_Update"

    @classmethod
    def all_events(cls) -> list[str]:
        return [attr for attr in dir(cls) if not attr.startswith("_")]